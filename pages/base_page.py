import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("BasePage")


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу {1}")
    def open(self, url=""):
        full_url = self.base_url + url
        logger.info(f"Открываю страницу: {full_url}")
        self.driver.get(full_url)

    @allure.step("Ищем элемент {1}")
    def find(self, locator):
        logger.info(f"Поиск элемента: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ищем элементы {1}")
    def finds(self, locator):
        logger.info(f"Поиск элементов: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликаем по элементу {1}")
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        logger.info(f"Клик по элементу: {locator}")
        element.click()

    @allure.step("Вводим текст '{2}' в элемент {1}")
    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        logger.info(f"Ввод текста '{text}' в элемент: {locator}")

    @allure.step("Проверяем видимость элемента {1}")
    def element_is_visible(self, locator):
        logger.info(f"Проверка видимости: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликаем по элементу через JS {1}")
    def js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)
        logger.info(f"JS-клик по элементу: {locator}")
