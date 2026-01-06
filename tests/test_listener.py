
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    # "appium:app": "C:/Users/User/Downloads/pnv.apk"
})

appium_server_url = 'http://localhost:4723'

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver) -> None:
        print(f'Finding {by} {value}')
        super().before_find(by, value, driver)

    def before_click(self, element, driver) -> None:
        print(f'Click on {element}')


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()



def test_swipe(driver):
    listener_driver = EventFiringWebDriver(driver, MyListener())
    while True:
        elements = listener_driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        print(elements[0].rect)

        listener_driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

        elements = listener_driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        element_names = [name.text for name in elements]
        print(element_names)

        if 'Camera' in element_names:
            break
