import psycopg2
from config import load_config


def add_part(part_name, vendor_list):
    config = load_config()

    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                # 1. insert part
                cur.execute(insert_part, (part_name,))
                part_id = cur.fetchone()[0]

                print("New part id:", part_id)

                # 2. assign vendors
                for vendor_id in vendor_list:
                    cur.execute(assign_vendor, (vendor_id, part_id))

                conn.commit()
                print("Transaction completed")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    add_part("Camera Module", (1, 2))