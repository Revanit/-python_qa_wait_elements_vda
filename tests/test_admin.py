import random
import allure
import logging

from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_products_page import AdminProductsPage

logger = logging.getLogger("AdminTests")


@allure.feature("Админка")
@allure.story("Авторизация")
@allure.title("Проверка входа и выхода из админ-панели")
def test_admin_login_logout(browser, base_url):
    login_page = AdminLoginPage(browser, base_url)

    with allure.step("Открываем страницу логина"):
        login_page.open_login()

    with allure.step("Выполняем вход в админку"):
        login_page.login()

    dashboard = AdminDashboardPage(browser, base_url)

    with allure.step("Закрываем модальное окно безопасности"):
        dashboard.close_security_modal()

    with allure.step("Проверяем, что мы на Dashboard"):
        logger.info(f"Текущий URL: {browser.current_url}")
        assert "dashboard" in browser.current_url.lower()

    with allure.step("Выходим из админ-панели"):
        dashboard.logout()

    with allure.step("Проверяем, что произошёл выход"):
        logger.info(f"Текущий URL: {browser.current_url}")
        assert "login" in browser.current_url.lower()


@allure.feature("Админка")
@allure.story("Управление товарами")
@allure.title("Добавление и удаление товара")
def test_add_delete_product(browser, base_url):
    login_page = AdminLoginPage(browser, base_url)

    with allure.step("Открываем страницу логина"):
        login_page.open_login()

    with allure.step("Выполняем вход в админку"):
        login_page.login()

    dashboard = AdminDashboardPage(browser, base_url)

    with allure.step("Закрываем модальное окно безопасности"):
        dashboard.close_security_modal()

    with allure.step("Переходим в раздел 'Products'"):
        dashboard.go_to_products()

    products_page = AdminProductsPage(browser, base_url)

    name = f"TestProduct_{random.randint(1000, 9999)}"
    model = f"Model_{random.randint(100, 999)}"
    keyword = f"seo-{random.randint(1000, 9999)}"

    with allure.step(f"Добавляем товар '{name}'"):
        products_page.add_product(name, "Meta Tag Title", model, keyword)

    with allure.step("Удаляем первый товар в списке"):
        products_page.delete_first_product()
