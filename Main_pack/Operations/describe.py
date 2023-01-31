import sqlite3

"hotel_management.db"
conn = sqlite3.connect("hotel_management.db")
print(conn)


def describe():

    query = '''pragma table_info(customers)
            '''

    details = conn.execute(query)
    for i in details:
        print(i)

