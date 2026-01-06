import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.command import Command

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    # "appium:app": "C:/Users/User/Downloads/pnv.apk"
})

appium_server_url = 'http://192.168.1.3:4723'

class ReportCommand(Command):
    GET_REPORT: str = "getReport"
    DELETE_REPORT: str = "deleteReport"
    SET_TEST_INFO: str = "setTestInfo"

@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()

def test_swipe(driver):
    driver.command_executor._commands = {**driver.command_executor._commands,
                                         ReportCommand.GET_REPORT: ("GET", "/getReport"),
                                         ReportCommand.DELETE_REPORT: ("DELETE", "/deleteReportData"),
                                         ReportCommand.SET_TEST_INFO: ("POST", "/setTestInfo"),
                                         }

    driver.execute(ReportCommand.DELETE_REPORT)
    try:
        while True:
            elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
            print(elements[0].rect)

            driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

            elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
            element_names = [name.text for name in elements]
            print(element_names)

            if 'Camera' in element_names:
                break
    finally:

        test_status = "PASSED" if 'Camera' in element_names else "FAILED"

        driver.execute(ReportCommand.SET_TEST_INFO,
                   {"sessionId": driver.session_id, "testName": 'test_one', "testStatus": test_status})
        html = driver.execute(ReportCommand.GET_REPORT)
        with open("report.html", "wt") as r:
            r.write(html['value'])
