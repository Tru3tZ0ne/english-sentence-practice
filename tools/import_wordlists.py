from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import random
import re
import shutil
import unicodedata
import zipfile
from collections import defaultdict
from io import BytesIO
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent
WORD_PATTERN = re.compile(r"^[A-Za-z][A-Za-z .,'’/&()\-]*$")
HEADWORD_PATTERN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
CORRUPTED_LETTERS = str.maketrans({"ɔ": "o", "ə": "e", "ŋ": "n", "æ": "a", "ʃ": "f"})


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value or ""))).strip()


def word_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("’", "'").casefold()).strip()


def meaning_key(value: str) -> str:
    return re.sub(r"[\s,，;；。]+", "", value.casefold()).strip()


def relationship_id(element: ET.Element) -> str:
    for name, value in element.attrib.items():
        if name.endswith("}id") or name == "id":
            return value
    raise ValueError("工作表缺少 relationship id")


class XlsxReader:
    def __init__(self, path: Path):
        self.path = path
        self.archive = zipfile.ZipFile(path)
        self.shared = self._shared_strings()
        self.sheets = self._sheet_paths()

    def close(self) -> None:
        self.archive.close()

    def _shared_strings(self) -> list[str]:
        try:
            root = ET.fromstring(self.archive.read("xl/sharedStrings.xml"))
        except KeyError:
            return []
        return ["".join(node.text or "" for node in item.findall(".//{*}t")) for item in root.findall("{*}si")]

    def _sheet_paths(self) -> dict[str, str]:
        workbook = ET.fromstring(self.archive.read("xl/workbook.xml"))
        relationships = ET.fromstring(self.archive.read("xl/_rels/workbook.xml.rels"))
        targets = {item.attrib["Id"]: item.attrib["Target"] for item in relationships.findall("{*}Relationship")}
        result: dict[str, str] = {}
        for sheet in workbook.findall(".//{*}sheet"):
            target = targets[relationship_id(sheet)].lstrip("/")
            if not target.startswith("xl/"):
                target = posixpath.normpath(posixpath.join("xl", target))
            result[sheet.attrib["name"]] = target
        return result

    @staticmethod
    def _column_number(reference: str) -> int:
        letters = re.match(r"[A-Z]+", reference)
        if not letters:
            return 0
        number = 0
        for character in letters.group():
            number = number * 26 + ord(character) - 64
        return number

    def rows(self, sheet_name: str):
        path = self.sheets[sheet_name]
        for _, row in ET.iterparse(BytesIO(self.archive.read(path)), events=("end",)):
            if not row.tag.endswith("}row"):
                continue
            values: dict[int, str] = {}
            for cell in row.findall("{*}c"):
                column = self._column_number(cell.attrib.get("r", ""))
                kind = cell.attrib.get("t")
                value_node = cell.find("{*}v")
                if kind == "inlineStr":
                    value = "".join(node.text or "" for node in cell.findall(".//{*}t"))
                elif value_node is None or value_node.text is None:
                    value = ""
                elif kind == "s":
                    value = self.shared[int(value_node.text)]
                else:
                    value = value_node.text
                values[column] = value
            yield int(row.attrib.get("r", "0")), values
            row.clear()


def repair_summary_row(word: str, phonetic: str, meaning: str) -> tuple[str, str, str] | None:
    word, phonetic, meaning = clean(word), clean(phonetic), clean(meaning)
    if any(character in word for character in "ɔəŋæʃ"):
        word = word.translate(CORRUPTED_LETTERS)
    if meaning:
        return word, phonetic, meaning
    match = HEADWORD_PATTERN.match(word)
    if not match or (len(match.group()) == 1 and word.upper() == match.group().upper()):
        return None
    headword = match.group()
    combined = clean(f"{word} {phonetic}")
    bracket = re.search(r"\[([^\]]+)]\s*(.+)$", combined)
    if not bracket:
        return None
    recovered_phonetic = f"/{clean(bracket.group(1))}/"
    recovered_meaning = clean(bracket.group(2)).replace("vt .", "vt.").replace("n .", "n.")
    return headword, recovered_phonetic, recovered_meaning


def part_of_speech(meaning: str) -> str:
    lowered = meaning.casefold().lstrip()
    for label, variants in (
        ("noun", ("n.", "n ")),
        ("verb", ("v.", "vt.", "vi.")),
        ("adjective", ("adj.", "a.")),
        ("adverb", ("adv.", "ad.")),
        ("preposition", ("prep.",)),
        ("conjunction", ("conj.",)),
        ("pronoun", ("pron.",)),
        ("number", ("num.",)),
    ):
        if lowered.startswith(variants):
            return label
    return "other"


def source_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_records(source_dir: Path) -> tuple[list[dict], dict]:
    configurations = [
        ("单词汇总-excel.xlsx", "Sheet1", 1, 3, 2, "summary"),
        ("六级词汇表.xlsx", "Sheet1", 1, 2, None, "standard"),
        ("雅思词汇EXCEL词-乱序版本.xlsx", "常用8000", 2, 7, None, "standard"),
        ("雅思词汇EXCEL词-乱序版本.xlsx", "全部9400", 1, 2, None, "standard"),
    ]
    required = {source_dir / item[0] for item in configurations}
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"缺少源文件：{missing}")
    readers: dict[Path, XlsxReader] = {}
    records: list[dict] = []
    skipped = defaultdict(int)
    extracted = defaultdict(int)
    sequence = 0
    try:
        for filename, sheet, word_column, meaning_column, phonetic_column, mode in configurations:
            path = source_dir / filename
            reader = readers.setdefault(path, XlsxReader(path))
            for row_number, row in reader.rows(sheet):
                raw_word = row.get(word_column, "")
                raw_meaning = row.get(meaning_column, "")
                raw_phonetic = row.get(phonetic_column, "") if phonetic_column else ""
                repaired = repair_summary_row(raw_word, raw_phonetic, raw_meaning) if mode == "summary" else (clean(raw_word), clean(raw_phonetic), clean(raw_meaning))
                if not repaired:
                    skipped["empty_or_header"] += 1
                    continue
                word, phonetic, meaning = repaired
                if not word or not meaning:
                    skipped["missing_word_or_meaning"] += 1
                    continue
                if not re.search(r"[\u4e00-\u9fff]", meaning):
                    skipped["missing_chinese_translation"] += 1
                    continue
                if not WORD_PATTERN.fullmatch(word) or len(re.sub("[^A-Za-z]", "", word)) < 2:
                    skipped["invalid_headword"] += 1
                    continue
                sequence += 1
                source_ref = f"{filename}/{sheet}/{row_number}"
                records.append({"word": word, "meaning": meaning, "phonetic": phonetic, "source": source_ref, "source_file": filename, "sheet": sheet, "sequence": sequence})
                extracted[f"{filename}/{sheet}"] += 1
    finally:
        for reader in readers.values():
            reader.close()
    return records, {"extracted": dict(extracted), "skipped": dict(skipped), "source_sha256": {path.name: source_hash(path) for path in sorted(required)}}


def build_words(records: list[dict]) -> tuple[list[dict], dict]:
    groups: dict[str, list[dict]] = {}
    for record in records:
        groups.setdefault(word_key(record["word"]), []).append(record)
    source_rank = {"全部9400": 0, "常用8000": 1, "六级词汇表.xlsx": 2, "单词汇总-excel.xlsx": 3}
    words: list[dict] = []
    conflicts = 0
    for key, entries in groups.items():
        meanings: list[str] = []
        seen_meanings: set[str] = set()
        for entry in entries:
            normalized = meaning_key(entry["meaning"])
            if normalized not in seen_meanings:
                meanings.append(entry["meaning"])
                seen_meanings.add(normalized)
        if len(meanings) > 1:
            conflicts += 1
        ranked = sorted(entries, key=lambda item: (source_rank.get(item["sheet"], source_rank.get(item["source_file"], 9)), -len(item["meaning"]), item["sequence"]))
        primary = ranked[0]
        main_key = meaning_key(primary["meaning"])
        alternatives = [meaning for meaning in meanings if meaning_key(meaning) != main_key]
        phonetic = next((entry["phonetic"] for entry in entries if entry["phonetic"]), "")
        identifier = "word_" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
        words.append({
            "id": identifier,
            "word": entries[0]["word"],
            "phonetic": phonetic,
            "meaning": primary["meaning"],
            "alternatives": alternatives,
            "sources": list(dict.fromkeys(entry["source"] for entry in entries)),
            "_sequence": min(entry["sequence"] for entry in entries),
        })
    words.sort(key=lambda item: item["_sequence"])
    for item in words:
        item.pop("_sequence")
    return words, {"unique_words": len(words), "duplicate_rows_removed": len(records) - len(words), "words_with_alternative_meanings": conflicts}


def add_choices(words: list[dict]) -> None:
    by_part: dict[str, list[dict]] = defaultdict(list)
    for word in words:
        by_part[part_of_speech(word["meaning"])].append(word)
    for word in words:
        seed = int(hashlib.sha256(word["id"].encode()).hexdigest()[:16], 16)
        rng = random.Random(seed)
        pool = list(by_part[part_of_speech(word["meaning"])])
        rng.shuffle(pool)
        selected: list[dict] = []
        used = {meaning_key(word["meaning"])}
        for candidate in pool + words:
            candidate_key = meaning_key(candidate["meaning"])
            if candidate["id"] != word["id"] and candidate_key not in used:
                selected.append(candidate)
                used.add(candidate_key)
                if len(selected) == 3:
                    break
        if len(selected) != 3:
            raise ValueError(f"无法为 {word['word']} 生成三个不同释义")
        options = [{"text": word["meaning"], "correct": True}] + [{"text": item["meaning"], "correct": False} for item in selected]
        rng.shuffle(options)
        word["options"] = options


def write_output(output_dir: Path, source_dir: Path, words: list[dict], audit: dict, day_size: int = 100) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    days = []
    for offset in range(0, len(words), day_size):
        number = offset // day_size + 1
        items = words[offset:offset + day_size]
        filename = f"day-{number:03d}.json"
        payload = {"schema_version": 1, "wordlist_id": "cet4_combined", "day": number, "items": items}
        (output_dir / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        days.append({"day": number, "file": filename, "count": len(items)})
    index = {
        "schema_version": 1,
        "id": "cet4_combined",
        "title": "四级目录综合词汇",
        "description": "合并指定目录中的三份 Excel，清理错列并去重；每 100 词为一个 Day。",
        "language": "en",
        "tags": ["单词", "四级目录", "综合词汇"],
        "day_size": day_size,
        "word_count": len(words),
        "day_count": len(days),
        "days": days,
    }
    (output_dir / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit.update({"source_directory": source_dir.name, "output": {"word_count": len(words), "day_count": len(days), "day_size": day_size, "last_day_count": days[-1]["count"]}})
    (output_dir / "audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_dir = output_dir.parent
    manifest = {"schema_version": 1, "wordlists": [{"id": index["id"], "index": f"{output_dir.name}/index.json"}]}
    (manifest_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="导入并去重 Excel 单词表")
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "content" / "wordlists" / "cet4_combined")
    args = parser.parse_args()
    records, extraction = import_records(args.source_dir.resolve())
    words, deduplication = build_words(records)
    add_choices(words)
    audit = {"raw_valid_records": len(records), **extraction, **deduplication}
    write_output(args.output.resolve(), args.source_dir.resolve(), words, audit)
    print(json.dumps(audit | {"days": (len(words) + 99) // 100, "last_day": len(words) % 100 or 100}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
