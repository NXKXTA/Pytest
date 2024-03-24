import pytest


def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        # isinstance(text, str) проверяет, является ли text строкой.
        raise ValueError("Строка должна быть строкой")

    if not text:
        return False

    if len(text) < 3 or not text.strip():
        # not text.strip() проверяет, содержит ли строка только пробелы.
        # Функция strip() удаляет все пробелы из начала и конца строки.
        return False

    text = text.lower()  # Приводим все буквы к нижнему регистру
    return text == text[::-1]


def test_is_palindrome_positive():
    assert is_palindrome("казак")
    assert is_palindrome("madam")
    assert is_palindrome("rotor")
    assert is_palindrome("racecar")


def test_is_palindrome_negative():
    assert not is_palindrome("hello")
    assert not is_palindrome("world")
    assert not is_palindrome("12345")
    assert not is_palindrome("")
    assert not is_palindrome(" ")
    assert not is_palindrome("    ")
    assert not is_palindrome(".,:;")
    assert not is_palindrome("привет")
    assert not is_palindrome("123привет")


def test_is_palindrome_exceptions():
    with pytest.raises(ValueError):
        is_palindrome(123)
    with pytest.raises(ValueError):
        is_palindrome(["a", "b", "c"])
    with pytest.raises(ValueError):
        is_palindrome(None)
