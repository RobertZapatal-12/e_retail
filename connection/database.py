import psycopg2
import os


def create_connection():
    """Create a connection to the PostgreSQL database.

    Returns:
        psycopg2.extensions.connection: A database connection object.
    """
    conn = psycopg2.connect(
        dbname=os.getenv("PGDATABASE", "e_retail"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "yarel"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        connect_timeout=5,
    )
    return conn


def get_connection():
    """Return a new database connection.

    Returns:
        psycopg2.extensions.connection: A database connection object.
    """
    return create_connection()
