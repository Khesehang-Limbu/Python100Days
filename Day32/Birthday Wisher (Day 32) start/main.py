import smtplib
import datetime as dt
import random

with open("./quotes.txt") as quote_file:
    quote = quote_file.readlines()

now = dt.datetime.now()
email = "khesehang81@gmail.com"
password = "hqiaozpmynpaxzcc"

today = now.weekday()
print(today)

if today == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="evilk507@gmail.com", msg=f"subject:Monday Motivation\n\n{random.choice(quote)}")





