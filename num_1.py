import pytest


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n.

    Args:
        n: Целое число.

    Returns:
        Факториал n.

    Raises:
        ValueError: Если n не является целым числом.
        TypeError: Если n меньше 0.
    """

    if not isinstance(n, int):
        # Проверка типа объекта
        # isinstance(object: Объект, тип которого нужно проверить,
        # type_or_types: Тип или кортеж типов, с которым нужно сравнить объект)
        raise ValueError("n должен быть целым числом")
    if n < 0:
        raise TypeError("n не может быть меньше 0")

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def test_factorial_positive():
    # Для неотрицательных чисел
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24


def test_factorial_negative():
    # Для отрицательных чисел
    with pytest.raises(TypeError):
        factorial(-1)


def test_factorial_not_int():
    # Для не int значений
    with pytest.raises(ValueError):
        factorial(3.14)
        factorial("abc")


# Пример использования
"""
number = int(input("Введите число: "))

try:
  factorial_result = factorial(number)
  print(f"Факториал числа {number} равен {factorial_result}")
except (ValueError, TypeError) as error:
  print(error)
"""
