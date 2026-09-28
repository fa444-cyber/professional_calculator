import pytest
from app.operation import Operation


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
    (-5, -5, -10),
])
def test_add(a, b, expected):
    assert Operation.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 5, -5),
    (-1, -1, 0),
    (100, 50, 50),
])
def test_subtract(a, b, expected):
    assert Operation.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (0, 5, 0),
    (-3, -3, 9),
])
def test_multiply(a, b, expected):
    assert Operation.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-10, 2, -5),
    (100, 4, 25),
])
def test_divide(a, b, expected):
    assert Operation.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Operation.divide(5, 0)