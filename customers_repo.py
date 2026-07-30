from database import get_connection
import datetime as datetime

class CustomersRepository:
    def __init__(self, conn=None):
        self.conn = conn or get_connection()

    def close(self):
            """Close the database connection if it exists."""
            if self.conn is not None:
                self.conn.close()

    def insert_customers(
        self,
        customer_id: int,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (customer_id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)",
                (customer_id, first_name, last_name, email, phone)
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_customer_addresses(
        self,
        address_id: int,
        customer_id: int,
        address_line1: str,
        address_line2: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customer_addresses (address_id, customer_id, address_line1, address_line2, city, state, postal_code, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (address_id, customer_id, address_line1, address_line2, city, state, postal_code, country)
            )
            self.conn.commit()
            print("Insertado correctamente")
         