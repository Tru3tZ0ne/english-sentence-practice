from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


class LibraryValidationError(ValueError):
    pass


@dataclass(frozen=True)
class LibraryItem:
    id: str
    zh: str
    en: str
    answers: tuple[str, ...]
    notes: str = ""
    tags: tuple[str, ...] = ()
    difficulty: int = 1

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "zh": self.zh, "en": self.en, "answers": list(self.answers),
                "notes": self.notes, "tags": list(self.tags), "difficulty": self.difficulty}


@dataclass(frozen=True)
class Library:
    schema_version: int
    id: str
    title: str
    description: str
    language: str
    tags: tuple[str, ...]
    items: tuple[LibraryItem, ...]
    source_file: str


def _text(value: Any, field: str, where: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise LibraryValidationError(f"{where} 缺少有效的 {field}")
    return value.strip()


def validate_library(data: Any, source_file: str) -> Library:
    if not isinstance(data, dict):
        raise LibraryValidationError("根节点必须是 JSON 对象")
    version = data.get("schema_version")
    if version != 1:
        raise LibraryValidationError(f"不支持的 schema_version：{version!r}（当前仅支持 1）")
    library_id = _text(data.get("id"), "id", "题库")
    if not ID_PATTERN.fullmatch(library_id):
        raise LibraryValidationError("题库 id 只能包含小写字母、数字、下划线和连字符")
    title = _text(data.get("title"), "title", "题库")
    raw_items = data.get("items")
    if not isinstance(raw_items, list) or not raw_items:
        raise LibraryValidationError("题库 items 必须是非空数组")
    seen: set[str] = set()
    items: list[LibraryItem] = []
    for number, raw in enumerate(raw_items, 1):
        where = f"第 {number} 项"
        if not isinstance(raw, dict):
            raise LibraryValidationError(f"{where} 必须是对象")
        item_id = _text(raw.get("id"), "id", where)
        if not ID_PATTERN.fullmatch(item_id):
            raise LibraryValidationError(f"{where} id 格式无效：{item_id}")
        if item_id in seen:
            raise LibraryValidationError(f"{where} item id 重复：{item_id}")
        seen.add(item_id)
        zh = _text(raw.get("zh"), "zh", where)
        en = _text(raw.get("en"), "en", where)
        answers = raw.get("answers", [en])
        if not isinstance(answers, list) or not answers or any(not isinstance(x, str) or not x.strip() for x in answers):
            raise LibraryValidationError(f"{where} answers 必须是非空字符串数组")
        cleaned_answers = tuple(dict.fromkeys(x.strip() for x in answers))
        if en not in cleaned_answers:
            cleaned_answers = (en, *cleaned_answers)
        tags = raw.get("tags", [])
        if not isinstance(tags, list) or any(not isinstance(x, str) for x in tags):
            raise LibraryValidationError(f"{where} tags 必须是字符串数组")
        difficulty = raw.get("difficulty", 1)
        if not isinstance(difficulty, int) or not 1 <= difficulty <= 5:
            raise LibraryValidationError(f"{where} difficulty 必须是 1 到 5 的整数")
        items.append(LibraryItem(item_id, zh, en, cleaned_answers, str(raw.get("notes", "")), tuple(tags), difficulty))
    library_tags = data.get("tags", [])
    if not isinstance(library_tags, list) or any(not isinstance(x, str) for x in library_tags):
        raise LibraryValidationError("题库 tags 必须是字符串数组")
    return Library(1, library_id, title, str(data.get("description", "")),
                   str(data.get("language", "en-US")), tuple(library_tags), tuple(items), source_file)
