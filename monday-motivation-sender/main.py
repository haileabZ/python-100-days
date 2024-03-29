# monday motivation sender app

import smtplib
import datetime as dt
from random import choice

# your email account
MY_EMAIL = "....@gmail.com"
# your app password 
MY_PASSWORD = "..." 

today = dt.datetime.now().weekday()

if today == 0:
    with open("quotes.txt") as txt_file:
        all_quotes = txt_file.readlines()
        quote = choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Sending motivational "
                                                                       f"quote every monday\n\n{quote}")


