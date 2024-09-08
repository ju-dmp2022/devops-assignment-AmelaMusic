from BE.calculator_helper import CalculatorHelper


import pytest

# class TestCalculator():
#     def test_first(self):
#         pass


class BaseTest:
    def setup_method(self):
        self.calculator = CalculatorHelper()

    def teardown_method(self):
        self.calculator = None


class TestCalculator(BaseTest):

    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 6),
        (3, -3, 0),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(self, a, b, expected):
        # Arrange
        calculator = CalculatorHelper()

        # Act
        result = self.calculator.add(a, b)

        # Assert
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (1, 3, -2),
        (4, -3, 7),
        (-1, 1, -2),
        (0, 0, 0),
    ])
    def test_subtract(self, a, b, expected):

        calculator = CalculatorHelper()

        result = self.calculator.subtract(a, b)

        assert result == expected

    def test_multiply(self):

        calculator = CalculatorHelper()

        result = calculator.multiply(3, 2)

        assert result == 6

    def test_divide(self):

        calculator = CalculatorHelper()

        result = calculator.divide(10, 2)

        assert result == 5

    def test_divide_by_zero(self):

        calculator = CalculatorHelper()

        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
