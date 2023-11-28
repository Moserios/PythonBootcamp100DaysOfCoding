from selenium import webdriver
from selenium.webdriver.common.by import By
import time

INSTA_URL = 'https://www.instagram.com/'
INSTA_LOGIN = 'username'
INSTA_PASS = '1234567890'
INSTA_PAGE = 'https://www.instagram.com/therock/'
FOLLOWERS_URL = 'https://www.instagram.com/therock/followers/'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.list_of_followers = []

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(2)
        login_field = self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
        login_field.send_keys(INSTA_LOGIN)
        time.sleep(2)
        pass_field = self.driver.find_element(By.XPATH, "//input[@aria-label='Password']")
        pass_field.send_keys(INSTA_PASS)
        time.sleep(2)
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(INSTA_PAGE)
        time.sleep(5)
        self.driver.get(FOLLOWERS_URL)
        time.sleep(5)
        self.list_of_followers = self.driver.find_elements(By.XPATH, './/div[text()="Follow"]')
        time.sleep(5)
        return self.list_of_followers

    def follow(self):
        for i in range(1, len(self.list_of_followers)):
            elementt = self.list_of_followers[i]
            # pprint(elementt)
            try:
                elementt.click()
                time.sleep(2)
            except:
                print("Something happened. Can't click the 'Follow' button")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()


# Solution without OOP

# driver = webdriver.Chrome()
# driver.get(INSTA_URL)
# time.sleep(2)
# login_field = driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
# login_field.send_keys(INSTA_LOGIN)
# time.sleep(2)
# pass_field = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
# pass_field.send_keys(INSTA_PASS)
# time.sleep(2)
# submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# submit_button.click()
# time.sleep(5)

# driver.get(INSTA_PAGE)
# time.sleep(5)
# driver.get(FOLLOWERS_URL)
# time.sleep(5)
# list_of_followers = driver.find_elements(By.XPATH, './/div[text()="Follow"]')
# time.sleep(5)


# for i in range(1, len(list_of_followers)):
#     elementt = list_of_followers[i]
#     print(elementt)
#     elementt.click()
#     time.sleep(2)
