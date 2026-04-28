import psycopg2
import json
import csv
from config import load_config


def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    group_name = input("Enter group (Family/Work/Friend/Other): ")
    phone = input("Enter phone: ")
    phone_type = input("Enter phone type (home/work/mobile): ")

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO groups(name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                """, (group_name,))

                cur.execute("""
                    SELECT id FROM groups
                    WHERE name = %s
                """, (group_name,))
                group_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts(name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                """, (name, email, birthday, group_id))

                contact_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (contact_id, phone, phone_type))

            conn.commit()

        print("Contact added successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def show_all_contacts():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        c.id,
                        c.name,
                        c.email,
                        c.birthday,
                        g.name,
                        p.phone,
                        p.type
                    FROM contacts c
                    LEFT JOIN groups g ON c.group_id = g.id
                    LEFT JOIN phones p ON c.id = p.contact_id
                    ORDER BY c.id;
                """)

                rows = cur.fetchall()

                print("\nPhoneBook:")
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def search_by_email():
    email_part = input("Enter email text to search: ")
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        c.name,
                        c.email,
                        c.birthday,
                        g.name,
                        p.phone,
                        p.type
                    FROM contacts c
                    LEFT JOIN groups g ON c.group_id = g.id
                    LEFT JOIN phones p ON c.id = p.contact_id
                    WHERE c.email ILIKE %s
                """, (f"%{email_part}%",))

                rows = cur.fetchall()

                print("\nSearch result:")
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def export_to_json():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        c.name,
                        c.email,
                        c.birthday,
                        g.name,
                        p.phone,
                        p.type
                    FROM contacts c
                    LEFT JOIN groups g ON c.group_id = g.id
                    LEFT JOIN phones p ON c.id = p.contact_id
                    ORDER BY c.id;
                """)

                rows = cur.fetchall()
                data = []

                for row in rows:
                    contact = {
                        "name": row[0],
                        "email": row[1],
                        "birthday": str(row[2]),
                        "group": row[3],
                        "phone": row[4],
                        "type": row[5]
                    }
                    data.append(contact)

                with open("contacts.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("Exported to contacts.json successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
def import_from_csv():
    config = load_config()

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)

            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    for row in reader:
                        cur.execute("""
                            INSERT INTO groups(name)
                            VALUES (%s)
                            ON CONFLICT (name) DO NOTHING
                        """, (row["group"],))

                        cur.execute("""
                            SELECT id FROM groups
                            WHERE name = %s
                        """, (row["group"],))
                        group_id = cur.fetchone()[0]

                        cur.execute("""
                            INSERT INTO contacts(name, email, birthday, group_id)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (name) DO NOTHING
                            RETURNING id
                        """, (
                            row["name"],
                            row["email"],
                            row["birthday"],
                            group_id
                        ))

                        result = cur.fetchone()

                        if result:
                            contact_id = result[0]

                            cur.execute("""
                                INSERT INTO phones(contact_id, phone, type)
                                VALUES (%s, %s, %s)
                            """, (
                                contact_id,
                                row["phone"],
                                row["type"]
                            ))

                conn.commit()

        print("Imported from contacts.csv successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
if __name__ == "__main__":
    import_from_csv()


if __name__ == "__main__":
    export_to_json()
