import time

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

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()


@allure.feature("Swipe Test")
@allure.story("Swipe to Camera")
def test_swipe(driver):

    while True:
        with allure.step("Поиск элементов"):
            elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
            print(elements[0].rect)

        with allure.step("Выполнение свайпа"):
            driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

        with allure.step("Поиск элементов после свайпа"):
            elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
            element_names = [name.text for name in elements]
            print(element_names)

        with allure.step("Проверка на наличие Camera"):
            if 'Camera' in element_names:
                break
    time.sleep(5)