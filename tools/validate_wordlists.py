from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.config import WORDLISTS_DIR
from app.content.wordlist_loader import WordlistLoader, WordlistValidationError


def normalized_word(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("’", "'").casefold()).strip()


def main() -> int:
    loader = WordlistLoader(WORDLISTS_DIR)
    wordlists = loader.load_all()
    if loader.errors:
        for error in loader.errors:
            print(f"ERROR {error['file']}: {error['message']}")
        return 1
    if not wordlists:
        print("ERROR: 没有可用单词库")
        return 1
    total_words = 0
    total_days = 0
    for wordlist_id, index in wordlists.items():
        ids: set[str] = set()
        words: set[str] = set()
        counted = 0
        try:
            for day in index["days"]:
                payload = loader.load_day(index, day["day"])
                if len(payload["items"]) > index["day_size"]:
                    raise WordlistValidationError(f"Day {day['day']} 超过 {index['day_size']} 词")
                for item in payload["items"]:
                    key = normalized_word(item["word"])
                    if item["id"] in ids:
                        raise WordlistValidationError(f"跨 Day 重复 id：{item['id']}")
                    if key in words:
                        raise WordlistValidationError(f"跨 Day 重复单词：{item['word']}")
                    ids.add(item["id"])
                    words.add(key)
                counted += len(payload["items"])
        except WordlistValidationError as exc:
            print(f"ERROR {wordlist_id}: {exc}")
            return 1
        if counted != index["word_count"]:
            print(f"ERROR {wordlist_id}: 实际 {counted} 词，索引记录 {index['word_count']} 词")
            return 1
        total_words += counted
        total_days += index["day_count"]
        print(f"OK {wordlist_id}: {counted} words / {index['day_count']} days")
    print(f"Validated {len(wordlists)} wordlists / {total_days} days / {total_words} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
