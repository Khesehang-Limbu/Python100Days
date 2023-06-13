from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "E:\\Development\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://orteil.dashnet.org/cookieclicker/")
# is_loading = True
#
# while is_loading:
#     try:
#         driver.find_element(By.ID, "loader")
#     except:
#         is_loading = False
#
# language_btn = driver.find_element(By.ID, "langSelect-EN")
# language_btn.click()
#
# is_loading = True
# while is_loading:
#     try:
#         driver.find_element(By.ID, "loader")
#     except:
#         is_loading = False
#
# cookie_btn = driver.find_element(By.ID, "bigCookie")
# while True:
#     time.sleep(0.2)
#     cookie_btn.click()
#     try:
#         unlocked_items = driver.find_elements(By.CSS_SELECTOR("#store .product,.enabled,.unlocked"))
#         for item in unlocked_items:
#             item.click()
#     except Exception:
#         continue

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
t = time.localtime().tm_sec
maxItem = 0
m = 0
store = driver.find_element(By.ID, "store")
s = time.time()
while time.time() <= s + 60 * 60:
    start = time.time()
    while time.time() <= start + 5:
        cookie.click()
    time.sleep(0.1)
    items = driver.find_elements(By.CSS_SELECTOR, "#store > div")
    for i in range(len(items)):
        if items[i].get_attribute("class") != "grayed":
            item1 = items[i].find_element(By.TAG_NAME, "b")
            price = int(item1.text.split("-")[1].replace(",", ""))
            if price > m:
                maxItem = items[i]
                m = price
    try:
        print(maxItem.text)
        maxItem.click()
    except Exception:
        continue

cookie_per_second = driver.find_element(By.ID, "cps")
print(f"{cookie_per_second.text}")