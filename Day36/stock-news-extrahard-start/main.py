import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "FB5EA2Q8LGOU9372"
URL = "https://www.alphavantage.co/query"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
}

stocks_data = requests.get(URL, parameters).json()
# yesterday = stocks_data["Time Series (Daily)"][next(iter(stocks_data["Time Series (Daily)"]))]
# next(iter(stocks_data["Time Series (Daily)"]))
stocks = [value for (key, value) in stocks_data["Time Series (Daily)"].items()]
yesterday_closing_stock_value = float(stocks[0]["4. close"])
day_before_yesterday_closing_stock_value = float(stocks[1]["4. close"])

# (yesterday, yesterday_stocks), *rest = stocks_data["Time Series (Daily)"].items()
# yesterday_closing_stock_value = float(yesterday_stocks["4. close"])
#
# (day_before_yesterday, stock_values) = rest[0]
# day_before_yesterday_opening_stock_value = float(stock_values["4. close"])

fluctutate_percentage = round(((yesterday_closing_stock_value - day_before_yesterday_closing_stock_value) / yesterday_closing_stock_value) * 100)

if fluctutate_percentage < 0:
    change_sign = "🔻"
    fluctutate_percentage = abs(fluctutate_percentage)
else:
    change_sign = "🔺"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if fluctutate_percentage > 0:
    parameters = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apikey": "6d8b386a3c3e4a63840c0df080190fd7",
    }
    news = requests.get("https://newsapi.org/v2/everything", parameters)
    news.raise_for_status()
    news_articles = news.json()
    # top_three_news = [news for news in news_articles["articles"] if news_articles["articles"].index(news) < 3]
    top_three_news = news_articles["articles"][0:3:1]
    print(len(top_three_news))

# ## STEP 3: Use https://www.twilio.com
# # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = "AC2249ed51b42ad63cbcd63a5e62b171f1"
    auth_token = "4ab8ddf96bd22be4df20dae9cb48de27"
    client = Client(account_sid, auth_token)
    for article in top_three_news:
        message = client.messages.create(
            body=f"\nTSLA: {change_sign}{fluctutate_percentage}\n\nHeadline: {article['title']}\n\nBrief: {article['description']}",
            from_="+13203616263",
            to="+9779863784674"
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
