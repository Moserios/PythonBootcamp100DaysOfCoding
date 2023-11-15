import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import import Keys

driver = webdriver.Chrome()

# URL = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver.get(URL)
# number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]') #(drive.find_element_by_css_selector("#articlecount a")
# print(number.text)

URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Sergey")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Molchun")
email = driver.find_element(By.NAME, "email")
email.send_keys("email@email.com")
# submit_button = driver.find_element(By.XPATH, "/html/body/form/button")
submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
# submit_button.submit()
time.sleep(5)
submit_button.click()


