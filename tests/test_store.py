import random
import allure
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@allure.feature("Валюта")
@allure.story("Смена валюты в магазине")
@allure.title("Проверка изменения валюты на EUR")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_currency(browser, base_url):
    page = MainPage(browser, base_url)

    with allure.step("Открываем главную страницу"):
        page.open("")

    with allure.step("Меняем валюту на евро"):
        page.change_currency("euro")


@allure.feature("Регистрация")
@allure.story("Регистрация нового пользователя")
@allure.title("Регистрация нового пользователя с валидными данными")
@allure.severity(allure.severity_level.BLOCKER)
def test_register_new_user(browser, base_url):
    page = RegistrationPage(browser, base_url)

    with allure.step("Открываем страницу регистрации"):
        page.open_registration()

    email = f"user_{random.randint(1000,9999)}@test.com"

    with allure.step(f"Регистрируем пользователя с email {email}"):
        page.register("DI", "Voe", email, "password123")
