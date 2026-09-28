from abc import ABC, abstractmethod
from app.operation import Operation


class Calculation(ABC):
    """Abstract base class representing a calculation."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self):
        """Perform the calculation and return the result."""
        pass  # pragma: no cover

    def __str__(self):
        return f"{self.__class__.__name__}({self.a}, {self.b}) = {self.execute()}"


class AddCalculation(Calculation):
    def execute(self):
        return Operation.add(self.a, self.b)


class SubtractCalculation(Calculation):
    def execute(self):
        return Operation.subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    def execute(self):
        return Operation.multiply(self.a, self.b)


class DivideCalculation(Calculation):
    def execute(self):
        return Operation.divide(self.a, self.b)


class CalculationFactory:
    """Factory for creating Calculation instances based on an operator string."""

    _calculations = {
        "+": AddCalculation,
        "-": SubtractCalculation,
        "*": MultiplyCalculation,
        "/": DivideCalculation,
    }

    @staticmethod
    def create_calculation(operator, a, b):
        calculation_class = CalculationFactory._calculations.get(operator)
        if calculation_class is None:
            raise ValueError(f"Unsupported operator: '{operator}'")
        return calculation_class(a, b)