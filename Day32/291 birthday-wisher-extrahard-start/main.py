##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = "khesehang81@gmail.com"
MY_PASSWORD = "hqiaozpmynpaxzcc"

# 1. Update the birthdays.csv
dates_df = pandas.read_csv("./birthdays.csv")
dates_dict = dates_df.to_dict(orient="records")
# print(dates_dict)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_month = today.month
today_day = today.day

matched_person = [match for match in dates_dict if today_month == match["month"] and today_day == match["day"]]

if len(matched_person) != 0:
    print(matched_person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_letter = random.choice(LETTERS)
    print(random_letter)
    with open(f"./letter_templates/{random_letter}") as letter:
        letter = letter.readlines()

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for match in matched_person:
            birthday_letter = ''.join(letter).replace("[NAME]", match["name"])
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=match["email"], msg=birthday_letter)



