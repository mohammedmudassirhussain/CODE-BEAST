import sqlite3

conn = sqlite3.connect("hotel_management.db")

print(conn)


def check_out(input_name):

    conn.execute("  delete from customers where fname = '"+input_name+"' ")
    print("check_out successfull")

    print(conn.total_changes)

    conn.commit()
    conn.close()

