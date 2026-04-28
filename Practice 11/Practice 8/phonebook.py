import psycopg2
from config import load_config


def call_add_contact(name, phone):
    sql = "CALL add_contact(%s, %s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
            conn.commit()
        print("Contact added successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def show_all_contacts():
    sql = "SELECT * FROM get_all_contacts()"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()

                print("\nPhoneBook:")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def search_contact(name):
    sql = "SELECT * FROM search_contact_by_name(%s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                rows = cur.fetchall()

                print("\nSearch result:")
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


if __name__ == "__main__":
    call_add_contact("Charlie", "555000")
    show_all_contacts()
    search_contact("Cha")