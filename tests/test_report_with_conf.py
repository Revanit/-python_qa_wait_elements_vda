
from appium.webdriver.common.appiumby import AppiumBy


def test_swipe_one(driver, report):
    while True:
        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        print(elements[0].rect)

        driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

        elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
        element_names = [name.text for name in elements]
        print(element_names)
        a = 3
        b = 3
        assert a == b

        if 'Camera' in element_names:
            break

