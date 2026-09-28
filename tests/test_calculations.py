import pytest
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    CalculationFactory,
)


@pytest.mark.parametrize("calc_class, a, b, expected", [
    (AddCalculation, 2, 3, 5),
    (SubtractCalculation, 10, 4, 6),
    (MultiplyCalculation, 3, 4, 12),
    (DivideCalculation, 10, 2, 5),
])
def test_calculation_execute(calc_class, a, b, expected):
    calculation = calc_class(a, b)
    assert calculation.execute() == expected


def test_divide_calculation_by_zero():
    calculation = DivideCalculation(5, 0)
    with pytest.raises(ValueError):
        calculation.execute()


@pytest.mark.parametrize("operator, calc_class", [
    ("+", AddCalculation),
    ("-", SubtractCalculation),
    ("*", MultiplyCalculation),
    ("/", DivideCalculation),
])
def test_factory_creates_correct_class(operator, calc_class):
    calculation = CalculationFactory.create_calculation(operator, 4, 2)
    assert isinstance(calculation, calc_class)


def test_factory_unsupported_operator():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation("^", 4, 2)


def test_calculation_str_representation():
    calculation = AddCalculation(2, 3)
    assert str(calculation) == "AddCalculation(2, 3) = 5"