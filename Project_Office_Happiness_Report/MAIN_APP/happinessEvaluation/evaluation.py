import sqlite3

conn = sqlite3.connect('office_happiness_database.db')


def user_data():
    report={}
    print("Welcome to the Office Happiness Software")
    print("enter the User Detailsd")
    u_id = input("Enter the User ID")
    fname = str(input("Enter the First name:"))
    lname= str(input("Enter the Last name:"))
    mail_id= input("Enter the Mail_id ")
    gender = input("Enter the Gender")
    contact= input("Enter the Contact no.")
    role= input("Enter the Role")
    department= input("Enter the Department")

    report["u_id"]=u_id
    report["fname"]= fname
    report["lname"]= lname
    report["mail_id"]= mail_id
    report["gender"]=gender
    report["contact"]=contact
    report["role"]=role
    report["department"]=department

# conn.execute("""Insert into user(u_id,fname,lname,mail_id,gender,contact,role,department)
# Values(?,?,?,?,?,?,?,?)
# """,report.get("u_id"),report.get("fname"), report.get("lname"), report.get("mail_id"),report.get("contact"),report.get("gender"),report.get("role"),report.get("department"))
    conn.execute("""
    INSERT INTO user(u_id, fname, lname, mail_id, gender, contact, role, department)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (report.get("u_id"), report.get("fname"), report.get("lname"), report.get("mail_id"), report.get("gender"),
    report.get("contact"), report.get("role"), report.get("department")))

    conn.commit()
    print("User Data Entered Successfully")
    return report



def get_happiness_data():
    report={}

    print("Enter employee happiness details")
    u_id=input("Enter Employee ID:")
    h_id = input("Enter Happiness ID:")
    date=input("Enter date:")

    print("Please enter your happiness details 😀:")
    work_life_bal=int(input("Rate Work-Life Balance on 1-5 🏠:"))
    communication = int(input("Rate Communication on 1-5 🗣️:"))
    team_colab = int(input("Rate Team Collaboration on 1-5 🤝:"))
    carr_satisfy = int(input("Rate Career Satisfaction on 1-5 📈:"))

    feedback = input("Please give your feedback: ")




    report["u_id"]=u_id
    report["h_id"] = h_id
    report["date"] = date
    report["work_life_bal"] = work_life_bal
    report["communication"] = communication
    report["team_colab"] = team_colab
    report["carr_satisfy"] = carr_satisfy
    report["feedback"] = feedback
    print(report)
    report["happiness_score"]=calc_score(report)


    conn.execute("""
    Insert into happiness(u_id,h_id,date,work_life_bal,communication,team_colab,carr_satisfy,happiness_score,feedback)
    Values (?,?,?,?,?,?,?,?,?)
    """,(report.get("u_id"),report.get("h_id"),report.get("date"),report.get("work_life_bal"),report.get("communication"),report.get("team_colab"),report.get("carr_satisfy"),report.get("happiness_score"),report.get("feedback")))
    conn.commit()
    print('Data entered successfully.')
    return report


def calc_score(report):
    score=(report.get("work_life_bal")+report.get("communication")+report.get("team_colab")+report.get("carr_satisfy"))/4
    print(score)
    return score