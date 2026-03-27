import psycopg2
from config import load_config


def insert_vendor(vendor_name):
    """Insert a new vendor into the vendors table"""
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    config = load_config()
    vendor_id = None

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))
                vendor_id = cur.fetchone()[0]

        print(f"Inserted vendor: {vendor_name} (id={vendor_id})")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    return vendor_id


def insert_many_vendors(vendor_list):
    """Insert multiple vendors"""
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, vendor_list)

        print("Inserted multiple vendors")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


if __name__ == '__main__':
    insert_vendor("3M Co.")

    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])