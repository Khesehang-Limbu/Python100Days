import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# To use environment variable, use os.environ.get("ENV_NAME")

# API_KEY = "9e61eb2e259751589e81722acddc98d6"
API_KEY = "69f04e4613056b159c2761a9d9e664d2"
MY_LAT = 27.717245
MY_LONG = 85.323959

# Twilio Credentials
account_sid = "AC2249ed51b42ad63cbcd63a5e62b171f1"
auth_token = "38e29116789e64d2425386b7f804c101"

# API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"]

# Shorten the list using List Comprehension
first_twelve_hours_list = [hour for hour in hourly_weather if hourly_weather.index(hour) <= 11]

# Alternatively
shortened_weather_list = hourly_weather[0:12]

will_rain = False

for weather in first_twelve_hours_list:
    condition_code = weather["weather"][0]["id"]
    # print(type(condition_code))
    if condition_code < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # proxy_client.session.proxies = {"https:" os.environ["https_proxy"]}
    # http_client = proxy_client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hey, It's going to rain today, bring an umbrella",
        from_="+13203616263",
        to="+9779863784674"
    )

    print(message.status)
