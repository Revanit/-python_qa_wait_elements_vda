import pytest
import pymysql


def pytest_addoption(parser):
    """Добавляем параметры для подключения к БД через CLI (опционально)"""
    parser.addoption("--host", action="store", default=None, help="Database host")
    parser.addoption("--port", action="store", default=None, type=int, help="Database port")
    parser.addoption("--database", action="store", default=None, help="Database name")
    parser.addoption("--user", action="store", default=None, help="Database user")
    parser.addoption("--password", action="store", default=None, help="Database password")


@pytest.fixture(scope="session")
def connection(request):
    """Создаём соединение с БД (один раз за сессию pytest)"""

    # Если параметры не переданы — берём дефолтные из docker-compose
    host = request.config.getoption("--host") or "127.0.0.1"  # или "mysql" если pytest в контейнере
    port = request.config.getoption("--port") or 3306
    database = request.config.getoption("--database") or "opencart"
    user = request.config.getoption("--user") or "root"
    password = request.config.getoption("--password") or "opencart"

    # Пробуем подключиться
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        print(f"Подключено к базе данных '{database}' на {host}:{port} пользователем '{user}'")
    except pymysql.MySQLError as e:
        pytest.exit(f"Ошибка подключения к базе данных: {e}")

    yield conn

    conn.close()
    print("Соединение с БД закрыто.")


