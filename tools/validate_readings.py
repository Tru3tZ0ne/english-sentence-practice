from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z]+", text.casefold()))


def has_word(text: str, word: str) -> bool:
    return bool(re.search(rf"(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])", text, re.IGNORECASE))


def validate(readings_root: Path, wordlists_root: Path) -> dict:
    index = json.loads((readings_root / "cet4_combined" / "index.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    articles: list[dict] = []
    ids: set[str] = set()
    titles: set[str] = set()
    openings: Counter[str] = Counter()
    expected_days = list(range(1, index.get("day_count", 0) + 1))
    if [entry.get("day") for entry in index.get("days", [])] != expected_days:
        errors.append("阅读 Day 必须从 1 连续到 95")
    for day in expected_days:
        reading_path = readings_root / "cet4_combined" / f"day-{day:03}.json"
        word_path = wordlists_root / "cet4_combined" / f"day-{day:03}.json"
        if not reading_path.exists():
            errors.append(f"Day {day} 缺少阅读文件")
            continue
        data = json.loads(reading_path.read_text(encoding="utf-8"))
        words = {item["word"].casefold() for item in json.loads(word_path.read_text(encoding="utf-8"))["items"]}
        if data.get("day") != day or len(data.get("articles", [])) != 3:
            errors.append(f"Day {day} 标识错误或不是 3 篇")
            continue
        if {article.get("type") for article in data["articles"]} != {"story", "explanatory", "opinion"}:
            errors.append(f"Day {day} 缺少指定体裁")
        for article in data["articles"]:
            article_id, title, text = article.get("id", ""), article.get("title", ""), article.get("text", "")
            if article_id in ids: errors.append(f"文章 id 重复：{article_id}")
            if title.casefold() in titles: errors.append(f"文章标题重复：{title}")
            ids.add(article_id); titles.add(title.casefold())
            count = len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", text))
            if not 60 <= count <= 175: errors.append(f"{article_id} 长度不合格：{count}")
            sentences = article.get("sentences", [])
            if len(sentences) < 4: errors.append(f"{article_id} 逐句对照不足四句")
            elif " ".join(item.get("en", "").strip() for item in sentences) != text: errors.append(f"{article_id} 逐句英文与正文不一致")
            target_words = article.get("target_words", [])
            if not 5 <= len(target_words) <= 9: errors.append(f"{article_id} 目标词数量不合格")
            for target in target_words:
                if target.get("word", "").casefold() not in words: errors.append(f"{article_id} 目标词不属于当天：{target.get('word')}")
                if not has_word(text, target.get("word", "")): errors.append(f"{article_id} 正文未出现目标词：{target.get('word')}")
            if len(article.get("questions", [])) != 2: errors.append(f"{article_id} 阅读题数量错误")
            if not re.search(r"[\u4e00-\u9fff]", article.get("translation", "")): errors.append(f"{article_id} 缺少中文译文")
            normalized = normalize(text)
            openings[" ".join(normalized.split()[:8])] += 1
            articles.append({"id": article_id, "text": normalized})
    duplicates = len(articles) - len({article["text"] for article in articles})
    if duplicates: errors.append(f"存在 {duplicates} 篇完全重复正文")
    repeated_openings = {opening: count for opening, count in openings.items() if count > 2}
    if repeated_openings: errors.append(f"有 {len(repeated_openings)} 组开头重复超过两次")
    near_pairs = []
    for left in range(len(articles)):
        for right in range(left + 1, len(articles)):
            a, b = articles[left], articles[right]
            length_ratio = min(len(a["text"]), len(b["text"])) / max(len(a["text"]), len(b["text"]))
            if length_ratio < .72:
                continue
            score = SequenceMatcher(None, a["text"], b["text"], autojunk=False).ratio()
            if score >= .72:
                near_pairs.append((a["id"], b["id"], round(score, 3)))
    if near_pairs: errors.append(f"存在 {len(near_pairs)} 对正文相似度不低于 72%")
    return {"days": len(expected_days), "articles": len(articles), "duplicates": duplicates, "repeated_openings": repeated_openings, "near_pairs": near_pairs, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="校验语境阅读数据及同质化")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(ROOT / "content" / "readings", ROOT / "content" / "wordlists")
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Days: {result['days']}  Articles: {result['articles']}  Duplicates: {result['duplicates']}  Near pairs: {len(result['near_pairs'])}")
        for error in result["errors"]: print(f"ERROR: {error}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
