from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "E:\\Development\\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("http://127.0.0.1:3000")
fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Khesehang")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Yonghang")

email = driver.find_element(By.NAME, "email")
email.send_keys("khesehang81@gmail.com")

submit = driver.find_element(By.TAG_NAME, "button")
submit.click()
# driver.quit()
