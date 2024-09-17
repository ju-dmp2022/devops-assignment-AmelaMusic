from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class RegistrationPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            'register_button': Element('//button[@id="register"]', self),
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password1"]', self),
            'confirm_password': Element('//input[@id="password2"]', self),
            'submit_register': Element('//button[@id="register"]', self),
        }

        self.elements = munchify(self.page_elements)

    def navigate_to_register(self):
        self.elements.register_button.click()

    def register(self, username, password, confirm_password):
        self.elements.username.set(username)
        self.elements.password.set(password)
        self.elements.confirm_password.set(confirm_password)
        self.elements.submit_register.click()
