import sqlite3
conn = sqlite3.connect('office_happiness_database.db')


def Gender_based_report(gen):
    gen = gen.capitalize()
    query = "SELECT * FROM user inner join happiness on user.u_id = happiness.u_id  where gender=?"
    record = conn.execute(query, (gen, ))

    for i in record:
        print(i)


