from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    AGREE = (By.NAME, "agree")
    CONTINUE_BTN = (By.CSS_SELECTOR, "button.btn-primary")

    def open_registration(self):
        self.open("/index.php?route=account/register")

    def register(self, firstname, lastname, email, password):
        self.type(self.FIRSTNAME, firstname)
        self.type(self.LASTNAME, lastname)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.js_click(self.AGREE)
        self.js_click(self.CONTINUE_BTN)
