from __future__ import annotations

import json
import logging
import re
from pathlib import Path


class WordlistValidationError(ValueError):
    pass


def _read_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WordlistValidationError(f"无法读取 {path.name}：{exc}") from exc
    if not isinstance(data, dict):
        raise WordlistValidationError(f"{path.name} 的根节点必须是对象")
    return data


def _safe_child(directory: Path, relative: str) -> Path:
    path = (directory / relative).resolve()
    if directory.resolve() not in path.parents:
        raise WordlistValidationError(f"文件路径越界：{relative}")
    return path


class WordlistLoader:
    def __init__(self, directory: Path):
        self.directory = directory
        self.errors: list[dict[str, str]] = []

    def load_all(self) -> dict[str, dict]:
        self.errors = []
        self.directory.mkdir(parents=True, exist_ok=True)
        manifest_path = self.directory / "manifest.json"
        if not manifest_path.is_file():
            return {}
        try:
            manifest = _read_json(manifest_path)
            if manifest.get("schema_version") != 1 or not isinstance(manifest.get("wordlists"), list):
                raise WordlistValidationError("manifest.json 格式不正确")
        except WordlistValidationError as exc:
            self.errors.append({"file": "manifest.json", "message": str(exc)})
            return {}

        result: dict[str, dict] = {}
        for entry in manifest["wordlists"]:
            filename = str(entry.get("index", "")) if isinstance(entry, dict) else ""
            try:
                index_path = _safe_child(self.directory, filename)
                index = self._validate_index(_read_json(index_path), index_path)
                if index["id"] in result:
                    raise WordlistValidationError(f"单词库 id 重复：{index['id']}")
                result[index["id"]] = index
            except WordlistValidationError as exc:
                self.errors.append({"file": filename or "manifest.json", "message": str(exc)})
                logging.error("单词库加载失败 %s: %s", filename, exc)
        return result

    def _validate_index(self, data: dict, path: Path) -> dict:
        if data.get("schema_version") != 1:
            raise WordlistValidationError(f"{path.name} schema_version 必须为 1")
        for field in ("id", "title"):
            if not isinstance(data.get(field), str) or not data[field].strip():
                raise WordlistValidationError(f"{path.name} 缺少 {field}")
        days = data.get("days")
        if not isinstance(days, list) or not days:
            raise WordlistValidationError(f"{path.name} 缺少 Days")
        expected = list(range(1, len(days) + 1))
        numbers = [item.get("day") for item in days if isinstance(item, dict)]
        if numbers != expected:
            raise WordlistValidationError(f"{path.name} 的 Day 编号必须从 1 连续递增")
        if data.get("day_count") != len(days):
            raise WordlistValidationError(f"{path.name} 的 day_count 与 Days 不一致")
        if data.get("word_count") != sum(item.get("count", 0) for item in days):
            raise WordlistValidationError(f"{path.name} 的 word_count 与 Days 不一致")
        for item in days:
            if not isinstance(item.get("file"), str) or not isinstance(item.get("count"), int):
                raise WordlistValidationError(f"{path.name} 包含无效 Day")
            _safe_child(path.parent, item["file"])
        return {**data, "_directory": str(path.parent)}

    def load_day(self, index: dict, day_number: int) -> dict:
        day = next((item for item in index["days"] if item["day"] == day_number), None)
        if day is None:
            raise WordlistValidationError(f"Day {day_number} 不存在")
        path = _safe_child(Path(index["_directory"]), day["file"])
        data = _read_json(path)
        if data.get("schema_version") != 1 or data.get("wordlist_id") != index["id"] or data.get("day") != day_number:
            raise WordlistValidationError(f"{path.name} 的标识与索引不一致")
        items = data.get("items")
        if not isinstance(items, list) or len(items) != day["count"]:
            raise WordlistValidationError(f"{path.name} 的单词数量与索引不一致")
        seen: set[str] = set()
        for position, item in enumerate(items, 1):
            if not isinstance(item, dict) or not all(isinstance(item.get(field), str) and item[field].strip() for field in ("id", "word", "meaning")):
                raise WordlistValidationError(f"{path.name} 第 {position} 个单词格式不正确")
            if not re.search(r"[\u4e00-\u9fff]", item["meaning"]):
                raise WordlistValidationError(f"{item['word']} 缺少中文释义")
            if item["id"] in seen:
                raise WordlistValidationError(f"{path.name} 存在重复 id：{item['id']}")
            seen.add(item["id"])
            options = item.get("options")
            if not isinstance(options, list) or len(options) != 4:
                raise WordlistValidationError(f"{item['word']} 必须有 4 个释义选项")
            texts = [option.get("text", "").strip() for option in options if isinstance(option, dict)]
            if len(texts) != 4 or len(set(texts)) != 4 or sum(option.get("correct") is True for option in options) != 1:
                raise WordlistValidationError(f"{item['word']} 的释义选项必须互不相同且只有一个正确答案")
            if any(not re.search(r"[\u4e00-\u9fff]", text) for text in texts):
                raise WordlistValidationError(f"{item['word']} 的选项缺少中文释义")
        return data
