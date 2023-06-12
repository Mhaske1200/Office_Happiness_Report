import sqlite3
conn = sqlite3.connect ("office_happiness_database.db")


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