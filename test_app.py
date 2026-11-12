import pytest

from app import add, divide, multiply, subtract


@pytest.mark.parametrize("a,b,result", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, result):
    assert add(a, b) == result


@pytest.mark.parametrize("a,b,result", [(7, 4, 3), (2, 8, -6), (-2, -3, 1)])
def test_subtract(a, b, result):
    assert subtract(a, b) == result


@pytest.mark.parametrize("a,b,result", [(3, 5, 15), (-2, 4, -8), (7, 0, 0)])
def test_multiply(a, b, result):
    assert multiply(a, b) == result


@pytest.mark.parametrize("a,b,result", [(9, 2, 4.5), (-6, 3, -2), (0, 5, 0)])
def test_divide(a, b, result):
    assert divide(a, b) == pytest.approx(result)


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль"):
        divide(1, 0)
