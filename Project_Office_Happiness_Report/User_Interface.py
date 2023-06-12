import sqlite3
import MAIN_APP.get_info_on_gender as g
import MAIN_APP.insert_user as u
import MAIN_APP.get_user_happiness_detail as d
import MAIN_APP.insert_happiness as a
import MAIN_APP.sad_emp as s
import MAIN_APP.happy_emp as h

print("-------------------WELCOME TO THE OFFICE HAPPINESS SOFTWARE--------------------")
while True:
    print("""
     -------🙏🏻 MENU 🙏🏻--------
         SELECT ONE CHOICE
      
    1.Enter User Details
    2.Enter Happiness Details
    3.Get User Details 📂
    4.Get Happiness Details 📄
    5.Get User & Happiness Details on Gender ♂️♀️
    6.Fetch Users who are 😔
    7.Fetch Users who are 😊
    8.Exit""")
    print("Choose any option from above menu:")
    ch = int(input())
    if ch == 1:
        print(u.user_data())
    elif ch==2:
        print(a.get_happiness_data())
    elif ch==3:
        d.display_user()
    elif ch==4:
        d.display_happiness()
    elif ch==5:
        ch = str(input("Enter Gender ♀️♂️ :: "))
        if(ch == 'MALE' or ch == 'male' or ch == 'FEMALE' or ch == 'female' or ch == 'Male' or ch == 'Female'):
            g.get_info_by_gender(ch)
        else:
            pass
    elif ch==6:
        s.search_sad_emp()
    elif ch==7:
        h.user_happy()
    elif ch==8:
        break
    else:
        pass