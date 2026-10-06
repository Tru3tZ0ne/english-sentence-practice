from __future__ import annotations

from app.content.wordlist_loader import WordlistLoader, WordlistValidationError


class WordlistService:
    def __init__(self, loader: WordlistLoader):
        self.loader = loader
        self.wordlists = loader.load_all()

    def summaries(self) -> list[dict]:
        fields = ("id", "title", "description", "language", "tags", "day_size", "word_count", "day_count", "days")
        return [{field: index.get(field) for field in fields} for index in self.wordlists.values()]

    def day(self, wordlist_id: str, day_number: int) -> dict:
        index = self.wordlists.get(wordlist_id)
        if index is None:
            raise WordlistValidationError("单词库不存在")
        return self.loader.load_day(index, int(day_number))
