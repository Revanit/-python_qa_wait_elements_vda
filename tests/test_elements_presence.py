import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_elements(driver, elements):
    wait = WebDriverWait(driver, 10)
    for by, value in elements:
        try:
            wait.until(EC.visibility_of_element_located((by, value)))
        except Exception as e:
            timestamp = int(time.time())
            screenshot_name = f"error_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
            print(f"Saved screenshot: {screenshot_name}")
            raise AssertionError(f"Element not found: {by} = {value}") from e


def test_main_page_elements(browser, base_url):
    browser.get(base_url)
    elements = [
        (By.ID, "logo"),
        (By.ID, "menu"),
        (By.NAME, "search"),
        (By.LINK_TEXT, "Desktops"),
        (By.CLASS_NAME, "product-thumb"),
    ]
    wait_for_elements(browser, elements)


def test_catalog_page_elements(browser, base_url):
    browser.get(base_url + "/index.php?route=product/category&path=20")
    elements = [
        (By.CLASS_NAME, "product-thumb"),
        (By.ID, "input-sort"),
        (By.ID, "input-limit"),
        (By.CLASS_NAME, "pagination"),
        (By.CLASS_NAME, "list-group"),
    ]
    wait_for_elements(browser, elements)


def test_product_page_elements(browser, base_url):
    browser.get(base_url + "/index.php?route=product/product&product_id=40")
    elements = [
        (By.ID, "content"),
        (By.ID, "button-cart"),
        (By.CLASS_NAME, "image"),
        (By.CLASS_NAME, "price"),
        (By.ID, "input-quantity"),
    ]
    wait_for_elements(browser, elements)


def test_admin_login_page_elements(browser, base_url):
    browser.get(base_url + "/admin")
    elements = [
        (By.ID, "input-username"),
        (By.ID, "input-password"),
        (By.CLASS_NAME, "btn-primary"),
        (By.TAG_NAME, "form"),
    ]
    wait_for_elements(browser, elements)


def test_registration_page_elements(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
    elements = [
        (By.ID, "input-firstname"),
        (By.ID, "input-lastname"),
        (By.ID, "input-email"),
        (By.ID, "input-password"),
        (By.NAME, "agree"),
    ]
    wait_for_elements(browser, elements)
