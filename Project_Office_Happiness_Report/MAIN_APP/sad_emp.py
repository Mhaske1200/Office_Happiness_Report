import sqlite3
conn = sqlite3.connect('office_happiness_database.db')


def search_sad_emp():
    record = conn.execute("SELECT * FROM user inner join happiness on user.u_id = happiness.u_id where happiness_score < 3")

    for i in record:
        print(i)