import sqlite3
import MAIN_APP as ma
from MAIN_APP.happinessEvaluation import evaluation as e
from MAIN_APP.displayReports import display_users as d
from MAIN_APP.Search_Reports import Sad_emp as se
from MAIN_APP.Search_Reports import Happy_emp as he
from MAIN_APP.Search_Reports import Gender_based_report as ge

print("-------------------WELCOME TO THE OFFICE HAPPINESS SOFTWARE--------------------")
while True:
    print("""
------- MENU --------
SELECT ONE CHOICE

1.Enter User Details
2.Enter Happiness Details
3.Get User Details
4.Get Happiness Details
5.Get User & Happiness Details on Gender
6.Fetch Users who are 😔
7.Fetch Users who are 😊
8.Exit""")
    print("Choose any option from above menu:")
    ch = int(input())
    if ch == 1:
        print(e.user_data())
    elif ch == 2:
        print(e.get_happiness_data())
    elif ch == 3:
        d.display_user()
    elif ch == 4:
        d.display_happiness()
    elif ch == 5:
        ge.Gender_based_report(input())
    elif ch == 6:
        se.search_sad_emp()
    elif ch == 7:
        he.search_happy_emp()
    elif ch == 8:
        break
    else:
        pass