from database import get_connection
import datetime as datetime


class OrdersRepository:
    def __init__(self, conn=None):
        self.conn = conn or get_connection()

    def close(self):
            """Close the database connection if it exists."""
            if self.conn is not None:
                self.conn.close()

    def insert_order_statuses(
        self,
        order_status_id: int,
        code: str,
        description: str
    ):
         with self.conn.cursor() as cur:
              cur.execute(
                  "INSERT INTO order_statuses (order_status_id, code, description) VALUES (%s, %s, %s)",
                  (order_status_id, code, description)
              )
              self.conn.commit()
              print("Insertado correctamente")