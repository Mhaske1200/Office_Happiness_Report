
import sqlite3

conn=sqlite3.connect("office_happiness_database.db")
print(conn)


print("HAPPINESS TABLE USER")
details=conn.execute("pragma table_info('user')")
print(details)
for i in details:
    print(i)

print("HAPPINESS TABLE INFORMATION")
details=conn.execute("pragma table_info('happiness')")
print(details)
for i in details:
    print(i)

