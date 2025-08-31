from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminProductsPage(BasePage):
    ADD_BTN = (By.CSS_SELECTOR, "a.btn.btn-primary[title='Add New']")
    SAVE_BTN = (By.CSS_SELECTOR, "button[title='Save']")
    TAB_GENERAL = (By.CSS_SELECTOR, "a[href='#tab-general']")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    TAB_SEO = (By.CSS_SELECTOR, "a[href='#tab-seo']")
    PRODUCT_NAME = (By.ID, "input-name-1")
    META_TAG = (By.ID, "input-meta-title-1")
    MODEL = (By.ID, "input-model")
    KEYWORD = (By.ID, "input-keyword-0-1")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    CHECKBOX_FIRST = (By.CSS_SELECTOR, "input[name='selected[]']")
    DELETE_BTN = (By.CSS_SELECTOR, "button[formaction*='product.delete']")

    def add_product(self, name, meta, model, keyword):
        self.click(self.ADD_BTN)
        self.click(self.TAB_GENERAL)
        self.type(self.PRODUCT_NAME, name)
        self.type(self.META_TAG, meta)
        self.click(self.TAB_DATA)
        self.type(self.MODEL, model)
        self.click(self.TAB_SEO)
        self.type(self.KEYWORD, keyword)
        self.click(self.SAVE_BTN)

    def delete_first_product(self):
        self.click(self.PRODUCTS_LINK)
        self.click(self.CHECKBOX_FIRST)
        self.click(self.DELETE_BTN)
        alert = self.driver.switch_to.alert
        alert.accept()
