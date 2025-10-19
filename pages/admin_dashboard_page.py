from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminDashboardPage(BasePage):
    MENU = (By.ID, "menu")
    CLOSE_SECURITY = (By.CSS_SELECTOR, "#modal-security .btn-close")
    LOGOUT = (By.ID, "nav-logout")
    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")

    def close_security_modal(self):
        try:
            self.click(self.CLOSE_SECURITY)
        except:
            pass

    def go_to_products(self):
        self.click(self.CATALOG_MENU)
        self.click(self.PRODUCTS_LINK)

    def logout(self):
        self.click(self.LOGOUT)
