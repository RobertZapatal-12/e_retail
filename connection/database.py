import psycopg2


def create_connection():
    """Create a connection to the PostgreSQL database.

    Returns:
        psycopg2.extensions.connection: A database connection object.
    """
    conn = psycopg2.connect(
        dbname="e_retail",
        user="postgres",
        password="yarel",
        host="localhost",
        port=5432,
    )
    return conn


def get_connection():
    """Return a new database connection.

    Returns:
        psycopg2.extensions.connection: A database connection object.
    """
    return create_connection()
