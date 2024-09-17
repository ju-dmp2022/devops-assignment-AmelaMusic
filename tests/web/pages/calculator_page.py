from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            'username': Element('//label[@id="user-name"]', self),
            'number1': Element('//button[@id="key-1"]', self),
            'number2': Element('//button[@id="key-2"]', self),
            'number3': Element('//button[@id="key-3"]', self),
            'number4': Element('//button[@id="key-4"]', self),
            'number5': Element('//button[@id="key-5"]', self),
            'number6': Element('//button[@id="key-6"]', self),
            'number7': Element('//button[@id="key-7"]', self),
            'number8': Element('//button[@id="key-8"]', self),
            'number9': Element('//button[@id="key-9"]', self),
            'number0': Element('//button[@id="key-0"]', self),
            'add_button': Element('//button[@id="key-add"]', self),
            'subtract_button': Element('//button[@id="key-subtract"]', self),
            'multiply_button': Element('//button[@id="key-multiply"]', self),
            'divide_button': Element('//button[@id="key-divide"]', self),
            'equals_button': Element('//button[@id="key-equals"]', self),
            'result': Element('//input[@id="calculator-screen"]', self),
            'history_button': Element('//button[@id="toggle-button"]', self),
            'history_items': Element('//textarea[@id="history"]', self)
        }

        self.elements = munchify(self.page_elements)

    def enter_number(self, number):
        for digit in str(number):
            button = self.elements.__getattr__(f'number{digit}')
            button.click()

    def perform_calculation(self, num1, operator, num2):
        self.enter_number(num1)
        if operator == 'add':
            self.add()
        elif operator == 'subtract':
            self.subtract()
        elif operator == 'multiply':
            self.multiply()
        elif operator == 'divide':
            self.divide()
        else:
            raise ValueError(f"Unsupported operator: {operator}")
        self.enter_number(num2)
        self.equals()

    def perform_multiple_calculations(self, operations):
        for num1, operator, num2 in operations:
            self.perform_calculation(num1, operator, num2)

    def add(self):
        self.elements.add_button.click()

    def subtract(self):
        self.elements.subtract_button.click()

    def multiply(self):
        self.elements.multiply_button.click()

    def divide(self):
        self.elements.divide_button.click()

    def equals(self):
        self.elements.equals_button.click()

    def get_result(self):
        return self.elements.result.value

    def open_history(self):
        self.elements.history_button.click()

    def get_history_items(self):
        history_text = self.elements.history_items.value

        history_items = history_text.split('\n')

        return history_items
