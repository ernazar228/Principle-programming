import psycopg2
from config import load_config

def connect(config):
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        conn = psycopg2.connect(**config)
        print("Connected to the PostgreSQL server.")

        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            print("Connection test result:", result[0])

        return conn

    except (psycopg2.DatabaseError, Exception) as error:
        print("Connection error:", error)
        return None

if __name__ == '__main__':
    config = load_config()
    conn = connect(config)

    if conn is not None:
        conn.close()