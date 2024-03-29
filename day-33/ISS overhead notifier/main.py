# API exercise  

import smtplib
import requests
from datetime import datetime
import time

# Your latitude
MY_LAT = 6.020605
# Your longitude
MY_LONG = 37.564110

# your email app password
MY_PASSOWRD = "..." 
# your email adress
MY_EMAIL = "..."


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude<= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and is_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSOWRD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,msg="Subject:Sunrise teller\n\nthe ISS is above "
                                                                          "you in the sky")
            

