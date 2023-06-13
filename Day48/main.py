from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by

chrome_driver_path = "E:\\Development\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option, service=service)

# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1?keywords=pressure%2Bcooker&qid=1686135740&s=amazon-devices&sprefix=pressure%2Bc%2Camazon-devices%2C396&sr=1-1&th=1")
# price = driver.find_element(by.By.CSS_SELECTOR, ".apexPriceToPay")
# print(price.text)
driver.get("https://www.python.org/")
event_times = driver.find_elements(by.By.CSS_SELECTOR, ".event-widget time")

events = driver.find_elements(by.By.CSS_SELECTOR, ".event-widget .menu li")
event_model = {}
count = 0

for event in events:
    event_model[events.index(event)] = {
        "date": f"2023-{event.find_element(by.By.TAG_NAME, 'time').text}",
        "name": event.find_element(by.By.TAG_NAME, "a").text,
    }
    count += 1
print(event_model)

driver.quit()
