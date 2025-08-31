import random
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


def test_change_currency(browser, base_url):
    page = MainPage(browser, base_url)
    page.open("")
    page.change_currency("euro")


def test_register_new_user(browser, base_url):
    page = RegistrationPage(browser, base_url)
    page.open_registration()
    email = f"user_{random.randint(1000,9999)}@test.com"
    page.register("DI", "Voe", email, "password123")
