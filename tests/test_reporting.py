import pytest
import allure
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    # "appium:app": "C:/Users/User/Downloads/pnv.apk"
})

appium_server_url = 'http://192.168.1.3:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()


@allure.title("Пролистываем до приложения Calendar")
def test_swipe(driver):
    element_names = []

    try:
        with allure.step("Находим элементы списка и делаем swipe"):
            while True:
                elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")

                if len(elements) < 2:
                    break  # если элементов меньше двух — прерываем

                # Логируем координаты
                for i, el in enumerate(elements):
                    allure.attach(str(el.rect), f"element_{i}_rect", allure.attachment_type.TEXT)

                # swipe между первыми двумя элементами
                driver.swipe(elements[1].rect['x'], elements[1].rect['y'],
                             elements[0].rect['x'], elements[0].rect['y'])

                element_names = [el.text for el in elements]

                # Логируем найденные названия
                allure.attach(", ".join(element_names), "current_screen_elements", allure.attachment_type.TEXT)

                if 'Calendar' in element_names:
                    break

        with allure.step("Проверяем, что Calendar найден"):
            assert 'Calendar' in element_names, "Приложение Calendar не найдено!"

    finally:
        # Скриншот в случае ошибки
        if 'Calendar' not in element_names:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, "screenshot", allure.attachment_type.PNG)
