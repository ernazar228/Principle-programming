import psycopg2
from config import load_config


def delete_part(part_id):
    """ Delete part by part id """

    rows_deleted = 0
    config = load_config()

    sql = "DELETE FROM parts WHERE part_id = %s"

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (part_id,))
                rows_deleted = cur.rowcount

            conn.commit()

    except Exception as e:
        print("Error:", e)

    return rows_deleted


if __name__ == "__main__":
    deleted = delete_part(2)
    print("Deleted rows:", deleted)