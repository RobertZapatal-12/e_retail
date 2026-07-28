from database import get_connection


class ProductRepository:
    def __init__(self, conn=None):
        self.conn = conn or get_connection()

    def insert_product(self, brand_id: int, name: str):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO public.brands (brand_id, name) VALUES (%s, %s)",
                (brand_id, name),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def get_version(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT version()")
            return cur.fetchone()
