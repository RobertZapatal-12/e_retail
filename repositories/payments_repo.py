from database import get_connection
import datetime as datetime


class PaymentsRepository:
    def __init__(self, conn=None):
        self.conn = conn or get_connection()

    def close(self):
        """Close the database connection if it exists."""
        if self.conn is not None:
            self.conn.close()

    def insert_payment_methods(
        self, payment_method_id: int, code: str, description: str
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO payment_methods (payment_method_id, code, description) VALUES (%s, %s, %s)",
                (payment_method_id, code, description),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_payment_statuses(
        self, payment_status_id: int, code: str, description: str
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO payment_statuses (payment_status_id, code, description) VALUES (%s, %s, %s)",
                (payment_status_id, code, description),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_payments(
        self,
        payment_id: int,
        order_id: int,
        payment_method_id: int,
        payment_status_id: int,
        provider: str,
        amount: float,
        currency_code: str,
        transaction_reference: str,
    ):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO payments (payment_id, order_id, payment_method_id, payment_status_id, provider, amount, currency_code, transaction_reference) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    payment_id,
                    order_id,
                    payment_method_id,
                    payment_status_id,
                    provider,
                    amount,
                    currency_code,
                    transaction_reference,
                ),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def insert_currencies(self, currency_code: str, name: str):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO currencies (currency_code, name) VALUES (%s, %s)",
                (currency_code, name),
            )
            self.conn.commit()
            print("Insertado correctamente")
