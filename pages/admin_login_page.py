from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminLoginPage(BasePage):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.CLASS_NAME, "btn-primary")

    def open_login(self):
        self.open("/admin")

    def login(self, username="admin", password="admin"):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
