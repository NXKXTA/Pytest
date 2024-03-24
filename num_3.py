import pytest


def count_repeating_chars(text: str) -> int:
    if not isinstance(text, str):
        raise ValueError("Строка должна быть строкой")

    if not text:
        return 0

    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    repeating_chars = 0
    for count in char_counts.values():
        if count > 1:
            repeating_chars += count - 1

    return repeating_chars


def test_count_repeating_chars():
    assert count_repeating_chars("abc") == 0
    assert count_repeating_chars("abca") == 1
    assert count_repeating_chars("abcab") == 2
    assert count_repeating_chars("aaabbbccc") == 6
    assert count_repeating_chars("") == 0

    with pytest.raises(ValueError):
        count_repeating_chars(123)
    with pytest.raises(ValueError):
        count_repeating_chars(["a", "b", "c"])
    with pytest.raises(ValueError):
        count_repeating_chars(None)
