import sqlite3

"hotel_management.db"

conn = sqlite3.connect("hotel_management.db")
print(conn)

single = [40,41,42,43,44,45,46,47,48,49]
double = [30,31,32,33,34,35,36,37,38,39]
triple = [20,21,22,23,24,25,26,27,28,29]
quad   = [10,11,12,13,14,15,16,17,18,19]

s1 = []
d1 = []
t1 = []
q1 = []

def input_data():
    fname = input("Enter First Name:")
    lname = input("Enter Last Name:")
    pno   = int(input("Enter Phone Number:"))
    email = input("Enter email address:")
    cid   = input("Enter Check-In date:")
    cod   = input("Enter Check-Out date:")
    tov   = input("Enter the type of Verification:")

    data = {}
    data['fname'] = fname
    data['lname'] = lname
    data['pno'] = pno
    data['email'] = email
    data['cid'] = cid
    data['cod'] = cod
    data['tov'] = tov

    conn.execute('''
            insert into customers(fname,lname,pno,email,cid,cod,tov) values(?,?,?,?,?,?,?)''',
            (data.get("fname"),data.get("lname"),data.get("pno"),data.get("email"),data.get("cid"),data.get("cod"),data.get("tov")))
    conn.commit()
    print("data inserted successfully")
    return data

