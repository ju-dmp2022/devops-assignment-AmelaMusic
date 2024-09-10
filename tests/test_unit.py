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
        # Act
        result = self.calculator.subtract(a, b)

        # Assert
        assert result == expected

    def test_multiply(self):
        # Act
        result = self.calculator.multiply(3, 2)

        # Assert
        assert result == 6

    def test_divide(self):
        # Act
        result = self.calculator.divide(10, 2)

        # Assert
        assert result == 5

    def test_divide_by_zero(self):

        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(10, 0)
