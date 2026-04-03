"""Keyword-based matching for developer errors."""

from __future__ import annotations

import re

from core.database import get_known_errors


def normalize_text(text: str) -> str:
    """Lowercase text and remove punctuation for simpler matching."""
    lowered_text = text.lower()
    cleaned_text = re.sub(r"[^a-z0-9]+", " ", lowered_text)
    return re.sub(r"\s+", " ", cleaned_text).strip()


def score_keyword_match(normalized_input: str, keyword: str) -> int:
    """Score how well one keyword or phrase matches the user input."""
    normalized_keyword = normalize_text(keyword)

    if not normalized_input or not normalized_keyword:
        return 0

    input_words = set(normalized_input.split())
    keyword_words = normalized_keyword.split()

    if normalized_keyword in normalized_input:
        return len(keyword_words) + 2

    overlap_count = sum(1 for word in keyword_words if word in input_words)
    return overlap_count


def match_error(error_message: str) -> dict[str, str | list[str]] | None:
    """Return the best matching known error, if one is found."""
    normalized_input = normalize_text(error_message)

    best_match = None
    best_score = 0

    for error in get_known_errors():
        score = sum(
            score_keyword_match(normalized_input, keyword)
            for keyword in error["keywords"]
        )

        if score > best_score:
            best_match = error
            best_score = score

    return best_match if best_score >= 2 else None
