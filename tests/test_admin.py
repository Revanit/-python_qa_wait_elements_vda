import random
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_products_page import AdminProductsPage


def test_admin_login_logout(browser, base_url):
    login_page = AdminLoginPage(browser, base_url)
    login_page.open_login()
    login_page.login()
    dashboard = AdminDashboardPage(browser, base_url)
    dashboard.close_security_modal()
    assert "dashboard" in browser.current_url.lower()
    dashboard.logout()
    assert "login" in browser.current_url.lower()


def test_add_delete_product(browser, base_url):
    login_page = AdminLoginPage(browser, base_url)
    login_page.open_login()
    login_page.login()
    dashboard = AdminDashboardPage(browser, base_url)
    dashboard.close_security_modal()
    dashboard.go_to_products()
    products_page = AdminProductsPage(browser, base_url)
    name = f"TestProduct_{random.randint(1000,9999)}"
    model = f"Model_{random.randint(100,999)}"
    keyword = f"seo-{random.randint(1000,9999)}"
    products_page.add_product(name, "Meta Tag Title", model, keyword)
    products_page.delete_first_product()
