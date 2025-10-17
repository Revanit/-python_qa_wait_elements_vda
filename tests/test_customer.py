from data_base.db_queries import (
    create_customer,
    get_customer_by_id,
    update_customer,
    delete_customer_by_id
)

def test_valid_create_customer(connection):
    """Позитивный тест: создание нового клиента"""

    new_customer = {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "telephone": "1234567890",
        "password": "hashed_password_here",
        "status": 1
    }
    customer_id = create_customer(connection, new_customer)
    customer = get_customer_by_id(connection, customer_id)
    assert customer is not None, "Клиент должен существовать после создания"


def test_valid_update_customer(connection):
    """Обновление данных существующего клиента"""

    customer_id = 7
    updated_data = {
        "firstname": "AliceUpdated",
        "lastname": "WonderlandUpdated",
        "email": "alice.updated@example.com",
        "telephone": "999888777"
    }
    update_customer(connection, customer_id, updated_data)
    customer = get_customer_by_id(connection, customer_id)
    assert customer["firstname"] == updated_data["firstname"]
    assert customer["lastname"] == updated_data["lastname"]
    assert customer["email"] == updated_data["email"]
    assert customer["telephone"] == updated_data["telephone"]




def test_invalid_update_nonexistent_customer(connection):
    """Обновление несуществующего клиента"""

    updated_data = {
        "firstname": "NoOne",
        "lastname": "Nobody",
        "email": "noone@example.com",
        "telephone": "0000000000"
    }

    customer_id = 999999
    update_customer(connection, customer_id, updated_data)
    customer = get_customer_by_id(connection, customer_id)
    assert customer is None


def test_valid_delete_customer(connection):
    """Удаление существующего клиента"""

    customer_data = {
        "firstname": "Bob",
        "lastname": "Builder",
        "email": "bob@example.com",
        "telephone": "444555666",
        "password": "hashed_password_here",
        "status": 1
    }
    customer_id = create_customer(connection, customer_data)
    customer = get_customer_by_id(connection, customer_id)
    assert customer is not None
    delete_customer_by_id(connection, customer_id)
    customer = get_customer_by_id(connection, customer_id)
    assert customer is None


def test_invalid_delete_customer(connection):
    """Удаление несуществующего клиента"""

    non_existent_id = 888888
    delete_customer_by_id(connection, non_existent_id)
    customer = get_customer_by_id(connection, non_existent_id)
    assert customer is None
