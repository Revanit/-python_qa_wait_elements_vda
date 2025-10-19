from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "a.dropdown-toggle")
    EURO = (By.LINK_TEXT, "€ Euro")
    POUND = (By.LINK_TEXT, "£ Pound Sterling")

    def change_currency(self, currency="euro"):
        self.click(self.CURRENCY_DROPDOWN)
        if currency.lower() == "euro":
            self.click(self.EURO)
        elif currency.lower() == "pound":
            self.click(self.POUND)
