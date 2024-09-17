import pytest
import time
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.registration_page import RegistrationPage
from tests.web.pages.calculator_page import CalculatorPage
from assertpy import assert_that

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWeb(WebBase):

    # 2.1 Register a new user

    def generate_unique_username(self):
        return f"user_{int(time.time())}"

    def test_register(self):
        registration_page = RegistrationPage(self.driver)
        unique_username = self.generate_unique_username()

        registration_page.navigate_to_register()
        registration_page.register(unique_username, '1234', '1234')

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "user-name"), unique_username)
        )

        calculator_page = CalculatorPage(self.driver)

        assert_that(calculator_page.elements.username.text).is_equal_to(
            unique_username)

    # 2.2 Verify the calculation methods

    def test_addition(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        calculator_page = CalculatorPage(self.driver)
        assert_that(calculator_page.elements.username.text).is_equal_to('admin')

        calculator_page.perform_calculation(4, 'add', 9)
        result = calculator_page.get_result()

        assert_that(result).is_equal_to('13')

    def test_subtraction(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        calculator_page = CalculatorPage(self.driver)
        assert_that(calculator_page.elements.username.text).is_equal_to('admin')

        calculator_page.perform_calculation(5, 'subtract', 3)
        result = calculator_page.get_result()

        assert_that(result).is_equal_to('2')

    def test_multiplication(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        calculator_page = CalculatorPage(self.driver)
        assert_that(calculator_page.elements.username.text).is_equal_to('admin')

        calculator_page.perform_calculation(5, 'multiply', 3)
        result = calculator_page.get_result()

        assert_that(result).is_equal_to('15')

    def test_division(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        calculator_page = CalculatorPage(self.driver)
        assert_that(calculator_page.elements.username.text).is_equal_to('admin')

        calculator_page.perform_calculation(6, 'divide', 3)
        result = calculator_page.get_result()

        assert_that(result).is_equal_to('2')

    # 2.3 Verify the history feature

    def test_history(self):
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')
        calculator_page = CalculatorPage(self.driver)
        assert_that(calculator_page.elements.username.text).is_equal_to('admin')

        operations = [
            (63, 'add', 3),
            (69, 'multiply', 5),
            (9, 'subtract', 9)
        ]
        calculator_page.perform_multiple_calculations(operations)

        calculator_page.open_history()

        history_items = calculator_page.get_history_items()

        assert_that(history_items).contains('63+3=66')
        assert_that(history_items).contains('69*5=345')
        assert_that(history_items).contains('9-9=0')
