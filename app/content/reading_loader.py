from __future__ import annotations

import json
import logging
from pathlib import Path


class ReadingValidationError(ValueError):
    pass


def _read_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReadingValidationError(f"无法读取 {path.name}：{exc}") from exc
    if not isinstance(data, dict):
        raise ReadingValidationError(f"{path.name} 的根节点必须是对象")
    return data


def _safe_child(directory: Path, relative: str) -> Path:
    path = (directory / relative).resolve()
    if directory.resolve() not in path.parents:
        raise ReadingValidationError(f"文件路径越界：{relative}")
    return path


class ReadingLoader:
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
            if manifest.get("schema_version") != 1 or not isinstance(manifest.get("collections"), list):
                raise ReadingValidationError("manifest.json 格式不正确")
        except ReadingValidationError as exc:
            self.errors.append({"file": "manifest.json", "message": str(exc)})
            return {}

        result: dict[str, dict] = {}
        for entry in manifest["collections"]:
            filename = str(entry.get("index", "")) if isinstance(entry, dict) else ""
            try:
                index_path = _safe_child(self.directory, filename)
                index = self._validate_index(_read_json(index_path), index_path)
                if index["id"] in result:
                    raise ReadingValidationError(f"阅读库 id 重复：{index['id']}")
                result[index["id"]] = index
            except ReadingValidationError as exc:
                self.errors.append({"file": filename or "manifest.json", "message": str(exc)})
                logging.error("阅读库加载失败 %s: %s", filename, exc)
        return result

    def _validate_index(self, data: dict, path: Path) -> dict:
        if data.get("schema_version") != 1:
            raise ReadingValidationError(f"{path.name} schema_version 必须为 1")
        for field in ("id", "title", "wordlist_id"):
            if not isinstance(data.get(field), str) or not data[field].strip():
                raise ReadingValidationError(f"{path.name} 缺少 {field}")
        days = data.get("days")
        if not isinstance(days, list) or not days:
            raise ReadingValidationError(f"{path.name} 缺少 Days")
        if [item.get("day") for item in days if isinstance(item, dict)] != list(range(1, len(days) + 1)):
            raise ReadingValidationError(f"{path.name} 的 Day 编号必须从 1 连续递增")
        if data.get("day_count") != len(days):
            raise ReadingValidationError(f"{path.name} 的 day_count 与 Days 不一致")
        if data.get("article_count") != sum(item.get("count", 0) for item in days):
            raise ReadingValidationError(f"{path.name} 的 article_count 与 Days 不一致")
        for item in days:
            if not isinstance(item.get("file"), str) or not isinstance(item.get("count"), int):
                raise ReadingValidationError(f"{path.name} 包含无效 Day")
            _safe_child(path.parent, item["file"])
        return {**data, "_directory": str(path.parent)}

    def load_day(self, index: dict, day_number: int) -> dict:
        day = next((item for item in index["days"] if item["day"] == day_number), None)
        if day is None:
            raise ReadingValidationError(f"Day {day_number} 不存在")
        path = _safe_child(Path(index["_directory"]), day["file"])
        data = _read_json(path)
        if data.get("schema_version") != 1 or data.get("collection_id") != index["id"] or data.get("day") != day_number:
            raise ReadingValidationError(f"{path.name} 的标识与索引不一致")
        articles = data.get("articles")
        if not isinstance(articles, list) or len(articles) != day["count"]:
            raise ReadingValidationError(f"{path.name} 的文章数量与索引不一致")
        seen: set[str] = set()
        for position, article in enumerate(articles, 1):
            if not isinstance(article, dict) or not all(
                isinstance(article.get(field), str) and article[field].strip()
                for field in ("id", "title", "type", "text", "translation")
            ):
                raise ReadingValidationError(f"{path.name} 第 {position} 篇文章格式不正确")
            if article["id"] in seen:
                raise ReadingValidationError(f"{path.name} 存在重复文章 id：{article['id']}")
            seen.add(article["id"])
            words, questions = article.get("target_words"), article.get("questions")
            sentences = article.get("sentences")
            if not isinstance(sentences, list) or len(sentences) < 4 or not all(
                isinstance(sentence, dict) and all(
                    isinstance(sentence.get(field), str) and sentence[field].strip() for field in ("en", "zh")
                ) for sentence in sentences
            ):
                raise ReadingValidationError(f"{article['id']} 至少需要四组逐句中英对照")
            if " ".join(sentence["en"].strip() for sentence in sentences) != article["text"]:
                raise ReadingValidationError(f"{article['id']} 的英文正文与逐句内容不一致")
            if "".join(sentence["zh"].strip() for sentence in sentences) != article["translation"]:
                raise ReadingValidationError(f"{article['id']} 的中文译文与逐句内容不一致")
            if not isinstance(words, list) or not words or not all(
                isinstance(word, dict) and isinstance(word.get("word"), str) and word["word"].strip()
                and isinstance(word.get("meaning"), str) and word["meaning"].strip()
                for word in words
            ):
                raise ReadingValidationError(f"{article['id']} 缺少目标词")
            if not isinstance(questions, list) or len(questions) < 2 or not all(
                isinstance(question, dict) and all(isinstance(question.get(field), str) and question[field].strip() for field in ("prompt", "answer"))
                for question in questions
            ):
                raise ReadingValidationError(f"{article['id']} 至少需要两道阅读题及答案")
        return data
