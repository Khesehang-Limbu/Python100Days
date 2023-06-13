from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\\Development\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

content_portal = driver.find_element(By.XPATH, '//*[@id="mp-other-content"]/ul/li[7]/b/a')
# content_portal.click()

search = driver.find_element(By.NAME, "search")
# print(search.get_attribute("placeholder"))
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
