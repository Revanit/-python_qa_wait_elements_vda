import os
import datetime
import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser type: chrome or firefox",
    )
    parser.addoption(
        "--base_url",
        action="store",
        default="http://localhost",
        help="Base URL for OpenCart (e.g., http://localhost)",
    )


@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    base_url = request.config.getoption("--base_url")

    if browser_type == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_type == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    driver.maximize_window()
    driver.base_url = base_url
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )

            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(
                screenshots_dir, f"{item.name}_{timestamp}.png"
            )
            driver.save_screenshot(file_path)
