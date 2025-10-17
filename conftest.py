import pytest
import threading
from echo_server import run_server


def pytest_addoption(parser):
    parser.addoption("--host", default="127.0.0.1")
    parser.addoption("--port", default="5000")


@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")


@pytest.fixture(scope="session")
def port(request):
    return request.config.getoption("--port")


@pytest.fixture(scope="session", autouse=True)
def start_server(host, port):
    thread = threading.Thread(target=run_server, args=(host, port), daemon=True)
    thread.start()
