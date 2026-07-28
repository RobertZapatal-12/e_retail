import psycopg2


def create_connection():
    conn = psycopg2.connect(
        dbname="e_retail",
        user="postgres",
        password="yarel",
        host="localhost",
        port=5432
    )
    return conn

def get_connection():
    return create_connection()

