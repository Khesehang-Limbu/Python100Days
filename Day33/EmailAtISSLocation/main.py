import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 27.717245
MY_LONG = 85.323959

MY_USERNAME = "khesehang81@gmail.com"
MY_PASSWORD = "lpvmpvowuauawczi"

def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_location = iss_response.json()

    iss_longitude = float(iss_location["iss_position"]["longitude"])
    iss_latitude = float(iss_location["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    response_data = response.json()
    sunrise = int(response_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response_data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour <= sunrise or current_hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USERNAME, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_USERNAME, to_addrs="evilking913@gmail.com", msg="Subject:ISS Above You\n\nThe International Space Station is above you and the time is night, so get out and see.")


