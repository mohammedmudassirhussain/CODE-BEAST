import sqlite3

conn = sqlite3.connect("hotel_management.db")

print(conn)

single = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
double = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
triple = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
quad   = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

s1 = []
d1 = []
t1 = []
q1 = []

def room():
    x = 0
    print('''
              Type of Room:
                1.Single
                2.double
                3.Triple
                4.Quad
    
            ''')
    op = int(input("Enter your Choice:"))

    while x == 0:
        if op == 1:
            print("Total Available Rooms = ",len(single))
            print('''Are You Sure For Your Booking?
                            1.YES
                            2.NO
                 ''')
            ch1 = int(input())

            if ch1 == 1:
                for i in single:
                    break
                s1.append(i)
                print(s1)
                single.remove(i)
                print(single)
            break
        elif op == 2:
            print("Available Rooms = ", len(double))

            break
        elif op == 3:
            print("Available Rooms = ",len(triple))
            booking()
            break
        elif op == 4:
            print("Available Rooms = ",len(quad))
            booking()
            break












