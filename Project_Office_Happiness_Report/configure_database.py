import sqlite3

con = sqlite3.connect('office_happiness_database.db')
con.execute('''create table user(
u_id integer primary key,
fname text not null Check(typeof(fname) = 'text'),
lname text not null Check(typeof(lname) = 'text'),
mail_id text not null Check(mail_id like '%@%.%'),
contact text not null Check(length(contact)=10),
gender text not null check(gender in('Male','Female','Other')),
role text not null check(role in('Manager','Associate','Trainee')),
department text not null check(department in('IT','L&D','PnC','Digital Engineering'))
)'''
)

con.execute('''create table happiness(
u_id integer,
h_id integer primary key,
date text not null,
work_life_bal INTEGER NOT NULL CHECK (work_life_bal >= 1 AND work_life_bal <= 5),
communication INTEGER NOT NULL CHECK (communication >= 1 AND communication <= 5),
team_colab INTEGER NOT NULL CHECK (team_colab >= 1 AND team_colab <= 5),
carr_satisfy INTEGER NOT NULL CHECK (carr_satisfy >= 1 AND carr_satisfy <= 5),
happiness_score INTEGER NOT NULL CHECK (happiness_score >= 1 AND happiness_score <= 5),
feedback text,
foreign key(u_id) references user(u_id))''')
con.commit()
con.close()