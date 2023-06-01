from pprint import pprint
from smtplib import SMTP
from bs4 import BeautifulSoup
import lxml
import requests

url = "https://www.amazon.com/CORSAIR-Gaming-Chair-Comfort-Design/dp/B07Y98Y4L6"
headers = {
    # "Accept-Language": "en-US,en;q=0.9",
    # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
amazon_product_html = requests.get(url=url, headers=headers).content
amazon_product_soup = BeautifulSoup(amazon_product_html, "lxml")
product_price = amazon_product_soup.select_one(".apexPriceToPay .a-offscreen").getText()[1::1]

if float(product_price) < 405:
    with SMTP("smtp.gmail.com", 587) as client:
        client.starttls()
        client.login(user="khesehang81@gmail.com", password="app_password")
        client.sendmail(from_addr="khesehang81@gmail.com", to_addrs="evilking913@gmail.com", msg="Price Drop Alert!!\n\nThe price for the chair is less than $405 at Amazon, purchase it")

# import requests
# import lxml
# from bs4 import BeautifulSoup
#
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
#
# response = requests.get(url, headers=header)
#
# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
#
# price = soup.find(class_="a-offscreen").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)