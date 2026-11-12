"""Небольшой калькулятор: приложение для проверки CI."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль запрещено")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("3 * 5 =", multiply(3, 5))
    print("9 / 2 =", divide(9, 2))
