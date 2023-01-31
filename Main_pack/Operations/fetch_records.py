import sqlite3

"hotel_management.db"

conn = sqlite3.connect("hotel_management.db")
print(conn)

def get_records():
    print("first name  last name   ph number\t\t email\t   check-in  check-out  type of verification")
    print('=======================================================================================')
    record = conn.execute("select * from customers")
    for i in record:
        print(i)
    conn.commit()


