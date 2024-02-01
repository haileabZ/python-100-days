

##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import pandas as pd
from random import choice

# your app password
MY_PASSOWRD = "your password"
# your email
MY_EMAIL = "abc@gmail.com"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


today = dt.datetime.now()
year = today.year
month = today.month
day = today.day

file = pd.read_csv("birthdays.csv").to_dict(orient="records")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

for d in file:
    if  d["month"] == month and d["day"] == day:
        rand_letter = choice(["letter_1.txt", "Letter_2.txt", "letter_3.txt"])
        with open(f"letter_templates/{rand_letter}", "r") as f:
            text_to_send = f.read()
            last_letter = text_to_send.replace("[NAME]", d["name"])
            email_of_person = d["email"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSOWRD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email_of_person,
                                msg=f"Subject: My heartfelt birthday wish\n\n{last_letter}")





