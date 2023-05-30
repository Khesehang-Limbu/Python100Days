import requests
import os
from twilio.rest import Client
from smtplib import SMTP, SMTP_SSL

ACCOUNT_SID = "AC2249ed51b42ad63cbcd63a5e62b171f1"
API_KEY = "b31c7d9362a928e9895e2d586b706d5c"
TWILIO_NUMBER = "+13203616263"
TO_NUMBER = "+9779863784674"
GMAIL_APP_PASS = "fucyhdehwjcdokxn"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def notify(self, price, departure_city, departure_airport, arrival_city, arrival_airport, outbound_date,
               inbound_date, is_step_over=False, step_over=0, via_city=""):
        client = Client(ACCOUNT_SID, API_KEY)
        if is_step_over:
            message = client.messages.create(
                body=f"Low Price Alert! Only £{price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {inbound_date} to {outbound_date}\n\nFlight has {step_over} step over, via {via_city}",
                from_=TWILIO_NUMBER,
                to=TO_NUMBER
            )
        else:
            message = client.messages.create(
                body=f"Low Price Alert! Only £{price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {inbound_date} to {outbound_date}",
                from_=TWILIO_NUMBER,
                to=TO_NUMBER
            )

    def send_emails(self, user, price, departure_city, departure_airport, arrival_city, arrival_airport, outbound_date,
                    inbound_date, is_step_over=False, step_over=0, via_city=""):
        with SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user="khesehang81@gmail.com", password=GMAIL_APP_PASS)
            url = f"https://www.google.co.uk/flights?hl=en#flt={departure_airport}.{arrival_airport}.{inbound_date}*{arrival_airport}.{departure_airport}.{outbound_date}"

            if not is_step_over:
                connection.sendmail(from_addr="khesehang81@gmail.com", to_addrs=user,
                                      msg=f"Flight Club\n\nLow Price Alert! Only £.{price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {inbound_date} to {outbound_date}\n{url}".encode('utf-8'))
            else:
                connection.sendmail(from_addr="khesehang81@gmail.com", to_addrs="evilking913@gmail.com",
                                    msg=f"Flight Club\n\nLow Price Alert! Only £{price} to fly from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, from {inbound_date} to {outbound_date}\n\nFlight has {step_over} step over, via {via_city}\n{url}".encode(
                                        'utf-8'))