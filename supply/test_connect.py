import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    print("Connected successfully")
    conn.close()
except Exception as e:
    print("Connection error:", repr(e))