from datetime import datetime


def create_customer(connection, customer_data: dict) -> int:
    """
    Создаёт нового клиента в таблице oc_customer.
    Возвращает ID созданного клиента.
    """

    sql = """
        INSERT INTO oc_customer
        (customer_group_id, store_id, language_id, firstname, lastname,
         email, telephone, password, status, date_added)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, (
            customer_data.get("customer_group_id", 1),
            customer_data.get("store_id", 0),
            customer_data.get("language_id", 1),
            customer_data["firstname"],
            customer_data["lastname"],
            customer_data["email"],
            customer_data["telephone"],
            customer_data["password"],
            customer_data.get("status", 1),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ))
        connection.commit()
        return cursor.lastrowid


def get_customer_by_id(connection, customer_id: int):
    """
    Возвращает клиента по ID или None.
    """
    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def delete_customer_by_id(connection, customer_id: int):
    """
    Удаляет клиента по ID.
    """
    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        connection.commit()

def update_customer(connection, customer_id: int, updated_data: dict):
    """
    Обновляет существующего клиента в таблице oc_customer.
    Поля, которые можно обновлять: firstname, lastname, email, telephone
    """
    sql = """
        UPDATE oc_customer
        SET firstname = %s,
            lastname = %s,
            email = %s,
            telephone = %s
        WHERE customer_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, (
            updated_data["firstname"],
            updated_data["lastname"],
            updated_data["email"],
            updated_data["telephone"],
            customer_id
        ))
        connection.commit()
