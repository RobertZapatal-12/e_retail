from database import get_connection


class ProductRepository:
    """Repository class for managing brand data in PostgreSQL."""

    def __init__(self, conn=None):
        """Initialize the repository with a database connection.

        Args:
            conn: An existing database connection. If None, a new one is created.
        """
        self.conn = conn or get_connection()

    def insert_product(self, brand_id: int, name: str):
        """Insert a new brand into the database.

        Args:
            brand_id: The identifier of the brand.
            name: The brand name to insert.
        """
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO public.brands (brand_id, name) VALUES (%s, %s)",
                (brand_id, name),
            )
            self.conn.commit()
            print("Insertado correctamente")

    def close(self):
        """Close the database connection if it exists."""
        if self.conn is not None:
            self.conn.close()

    def get_version(self):
        """Return the PostgreSQL server version.

        Returns:
            tuple: A tuple containing the database version information.
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT version()")
            return cur.fetchone()
