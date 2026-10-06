from __future__ import annotations

import json
import logging
from pathlib import Path

from .schema import Library, LibraryValidationError, validate_library


class LibraryLoader:
    def __init__(self, directory: Path):
        self.directory = directory
        self.errors: list[dict[str, str]] = []

    def load_all(self) -> dict[str, Library]:
        self.errors = []
        result: dict[str, Library] = {}
        self.directory.mkdir(parents=True, exist_ok=True)
        for path in sorted(self.directory.glob("*.json")):
            try:
                with path.open("r", encoding="utf-8-sig") as handle:
                    library = validate_library(json.load(handle), path.name)
                if library.id in result:
                    raise LibraryValidationError(f"题库 id 与 {result[library.id].source_file} 重复：{library.id}")
                result[library.id] = library
            except (OSError, json.JSONDecodeError, LibraryValidationError) as exc:
                message = str(exc)
                self.errors.append({"file": path.name, "message": message})
                logging.error("题库加载失败 %s: %s", path.name, message)
        return result
