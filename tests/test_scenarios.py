import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_logout(browser, base_url):
    browser.get(base_url + "/admin")
    browser.find_element(By.ID, "input-username").send_keys("admin")
    browser.find_element(By.ID, "input-password").send_keys("admin")
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "menu")))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-security .btn-close"))
    ).click()
    assert "dashboard" in browser.current_url.lower()
    browser.find_element(By.ID, "nav-logout").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input-username"))
    )


def test_add_random_item_to_cart(browser, base_url):
    browser.get(base_url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    products = browser.find_elements(By.CLASS_NAME, "product-thumb")
    assert products
    product = random.choice(products)
    try:
        btn = product.find_element(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
    except:
        raise AssertionError("Кнопка 'Add to Cart' не найдена в выбранном товаре")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(btn))
    browser.execute_script("arguments[0].click();", btn)
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "button.btn.btn-lg.btn-dark.dropdown-toggle"), "1 item"
        )
    )


def test_currency_change_main(browser, base_url):
    browser.get(base_url)
    old_price = browser.find_element(By.CLASS_NAME, "price").text
    browser.find_element(By.CSS_SELECTOR, "a.dropdown-toggle").click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "€ Euro"))
    ).click()
    WebDriverWait(browser, 10).until_not(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "price"), old_price)
    )


def test_currency_change_catalog(browser, base_url):
    browser.get(base_url + "/index.php?route=product/category&path=20")
    old_price = browser.find_element(By.CLASS_NAME, "price").text
    browser.find_element(By.CSS_SELECTOR, "a.dropdown-toggle").click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "£ Pound Sterling"))
    ).click()
    WebDriverWait(browser, 10).until_not(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "price"), old_price)
    )
