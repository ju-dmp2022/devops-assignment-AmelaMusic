import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse


class BaseCalculatorTest:
    def setup_method(self):
        self.client = Client(base_url="http://localhost:5000")

    def teardown_method(self):
        self.client = None


class TestCalculatorAPI(BaseCalculatorTest):
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add",
            "operand1": 0,
            "operand2": 0
        }
        response = requests.post(url, json=payload)

    def test_auto_generated_add(self):
        # Reusing the client initialized in BaseCalculatorTest
        response = calculate.sync(client=self.client, body=Calculation(
            Opertions.ADD, operand1=1, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 2

    def test_calculate_subtraction(self):
        response = calculate.sync(client=self.client, body=Calculation(
            Opertions.SUBTRACT, operand1=4, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 3

    def test_calculate_multiply(self):
        response = calculate.sync(client=self.client, body=Calculation(
            Opertions.MULTIPLY, operand1=2, operand2=3))
        assert isinstance(response, ResultResponse)
        assert response.result == 6

    def test_calculate_divide(self):
        response = calculate.sync(client=self.client, body=Calculation(
            Opertions.DIVIDE, operand1=10, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 5
