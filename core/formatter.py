"""Formatting helpers for display output."""


def format_error_output(match: dict[str, str | list[str]]) -> list[tuple[str, str]]:
    """Convert a matched error into UI-friendly sections."""
    return [
        ("Meaning", str(match["meaning"])),
        ("Fix", str(match["fix"])),
        ("Why it happened", str(match["why_it_happened"])),
    ]


def format_no_match_message(_: str) -> str:
    """Message shown when no error match is found."""
    return (
        "No close match was found. Try pasting the most important part of the "
        "error message, such as `failed to push some refs` or `permission denied`."
    )
