import sqlite3

con = sqlite3.connect('office_happiness_database.db')
con.execute('''create table user(u_id int primary key,
               fname text not null Check(fname like = '%.[a-z,A-Z']'),
               lname text not null Check(lname like = '%.[a-z,A-Z']'),
               mail_id text not null Check(mail_id like = '%@%.%'),
               gender text not null,
               contact text not null Check(contact like = '[0-9]{10}'),
               role text not null,
               department text not null)''')

con.execute('''create table happiness(h_id int primary key,
               date text not null,
               work_life_bal text not null,
               communication text not null,
               team_colab text not null,
               carr_satisfy not null,
               happiness_score text not null,
               feedback text )''')
con.commit()
con.close()

