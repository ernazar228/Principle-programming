import psycopg2
from config import load_config


def connect():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            print("Connected to the PostgreSQL server.")
            
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                db_version = cur.fetchone()
                print(db_version)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


if __name__ == "__main__":
    connect()