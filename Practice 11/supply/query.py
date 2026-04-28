import psycopg2
from config import load_config


def get_part_vendors():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name;
                """)

                rows = cur.fetchall()
                print("Rows found:", len(rows))

                for row in rows:
                    print(row)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    get_part_vendors()