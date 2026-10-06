from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

TERMINAL = ".!?"


def normalize_answer(text: str, ignore_terminal_punctuation: bool = True) -> str:
    value = unicodedata.normalize("NFKC", text or "")
    value = value.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "，": ",", "。": ".", "！": "!", "？": "?"}))
    value = re.sub(r"\s+", " ", value.strip()).casefold()
    if ignore_terminal_punctuation:
        value = re.sub(r"[.!?]+$", "", value).rstrip()
    return value


@dataclass(frozen=True)
class CheckResult:
    correct: bool
    matched_answer: str | None
    normalized_input: str


class AnswerChecker:
    def check(self, user_answer: str, accepted: list[str] | tuple[str, ...], ignore_terminal_punctuation: bool = True) -> CheckResult:
        normalized = normalize_answer(user_answer, ignore_terminal_punctuation)
        for answer in accepted:
            if normalized and normalized == normalize_answer(answer, ignore_terminal_punctuation):
                return CheckResult(True, answer, normalized)
        return CheckResult(False, None, normalized)
