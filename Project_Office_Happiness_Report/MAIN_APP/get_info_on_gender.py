import sqlite3

conn = sqlite3.connect('office_happiness_database.db')


def get_info_by_gender(gen):

    query = "SELECT * from user u JOIN happiness h on u.u_id == h.h_id and u.gender == ? "
    records = conn.execute(query, (gen,))

    for i in records:
        print(i)

