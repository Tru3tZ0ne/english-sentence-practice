from __future__ import annotations

from app.content.reading_loader import ReadingLoader, ReadingValidationError


class ReadingService:
    def __init__(self, loader: ReadingLoader):
        self.loader = loader
        self.collections = loader.load_all()

    def summaries(self) -> list[dict]:
        fields = ("id", "title", "description", "wordlist_id", "tags", "article_count", "day_count", "days")
        return [{field: index.get(field) for field in fields} for index in self.collections.values()]

    def day(self, collection_id: str, day_number: int) -> dict:
        index = self.collections.get(collection_id)
        if index is None:
            raise ReadingValidationError("阅读库不存在")
        return self.loader.load_day(index, int(day_number))
