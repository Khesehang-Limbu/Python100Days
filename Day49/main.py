from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "E:\\Development\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=option)

driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3633359336&f_AL=true&f_E=2")
driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()

username = "evilking913@gmail.com"
password = "evilking123"

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "div btn__primary-large").click()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# ACCOUNT_EMAIL = YOUR LOGIN EMAIL
# ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
# PHONE = YOUR PHONE NUMBER
#
# chrome_driver_path = YOUR CHROME DRIVER PATH
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
#
# time.sleep(2)
# sign_in_button = driver.find_element_by_link_text("Sign in")
# sign_in_button.click()
#
# time.sleep(5)
# email_field = driver.find_element_by_id("username")
# email_field.send_keys(ACCOUNT_EMAIL)
# password_field = driver.find_element_by_id("password")
# password_field.send_keys(ACCOUNT_PASSWORD)
# password_field.send_keys(Keys.ENTER)
#
# time.sleep(5)
#
# all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#     try:
#         apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#         apply_button.click()
#
#         time.sleep(5)
#         phone = driver.find_element_by_class_name("fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         submit_button = driver.find_element_by_css_selector("footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             close_button.click()
#
#             time.sleep(2)
#             discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         time.sleep(2)
#         close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()
