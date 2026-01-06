import time

import pytest
from appium.webdriver import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common.base import AppiumOptions

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








def test_swipe(driver):

    while True:
        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        print(elements[0].rect)

        driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        element_names = [name.text for name in elements]
        print(element_names)

        if 'Camera' in element_names:
            break
    time.sleep(3)






# Если прмиенить метод скрола  то получается
# driver.scroll(elements[1], elements[0])


def test_scroll(driver):

    while True:
        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        print(elements[0].rect)

        driver.scroll(elements[1], elements[0])
        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        element_names = [name.text for name in elements]
        print(element_names)

        if 'Camera' in element_names:
            break

