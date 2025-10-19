import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type: chrome or firefox")
    parser.addoption("--browser_version", action="store", default="latest", help="Browser version")
    parser.addoption("--executor", action="store", default="local", help="Executor (local or selenoid)")
    parser.addoption("--opencart_url", action="store", default="http://localhost:8080", help="OpenCart base URL")


@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    base_url = request.config.getoption("--opencart_url")

    if browser_type == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--user-data-dir=/tmp/chrome-data")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser_type == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    driver.base_url = base_url
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--opencart_url")
