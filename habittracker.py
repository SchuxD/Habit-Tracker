from datetime import datetime
import pandas as pd
from tabulate import tabulate

def newhabit():
    global habitname
    global start_date
    global streak
    habitname = input("What habit would you like to start tracking? ")
    x = input("Did this habit occur today? ")
    if (x == 'yes' or "Yes"):
        print("Good job!")
        start_date = datetime.now()
        streak = 1
    return {"Habit": habitname, "Start Date": start_date, "No. of Days Completed": streak}

habits = [newhabit()]

df = pd.DataFrame(habits)
print(tabulate(df, headers="keys", tablefmt="psql"))



