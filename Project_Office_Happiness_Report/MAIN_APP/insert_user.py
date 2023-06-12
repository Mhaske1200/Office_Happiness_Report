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
    department= input("Enter the Department(IT','L&D','PnC','Digital Engineering)")

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