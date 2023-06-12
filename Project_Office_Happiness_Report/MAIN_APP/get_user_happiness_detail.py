import sqlite3

conn = sqlite3.connect('office_happiness_database.db')

def display_user():
    records= conn.execute("select * from user")
    for i in records:
        print(i)

def display_happiness():
    records= conn.execute("select * from happiness")
    for i in records:
        print(i)