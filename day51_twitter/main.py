from selenium import webdriver
from selenium.webdriver.common.by import By
import time

MIN_DOWNLOAD_SPEED = 150
MIN_UPLOAD_SPEED = 10
TWITTER_EMAIL = "sergemoseratti@gmail.com"
TWITTER_PASS = "1234567890"
SPEED_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/'

real_down = 0
real_up = 0


# IMPLEMENTED AS ROW CODE

# driver = webdriver.Chrome()
#
# # SPEEDTEST PART
# driver.get(SPEED_URL)
# driver.maximize_window()
# element = driver.find_element(By.CSS_SELECTOR, '.start-text')
# element.click()
# time.sleep(55)
# results = driver.find_element(By.CLASS_NAME, 'result-container-speed')
# real_down = (float(results.text.split()[2]))
# real_up = (float(results.text.split()[5]))
# print(real_down, real_up)
#
#
# # TWITTER PART
# driver.get(TWITTER_URL)
# time.sleep(5)
# login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
#
# login_button.click()
# time.sleep(3)
# email_field = driver.find_element(By.XPATH, '//input[@name="text"]')
# email_field.send_keys(TWITTER_EMAIL)
# email_submit_button = driver.find_element(By.XPATH, '//div[@role="button" and contains(., "Next")]')
# email_submit_button.click()
# time.sleep(10)
#
#   """Note: during login twitter could ask to enter additionally username or requested a password two times"""
#
# password_field = driver.find_element(By.XPATH, "//input[@name='password']")
# password_field.send_keys(TWITTER_PASS)
# time.sleep(2)
# password_submit_button = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
# password_submit_button.click()
# time.sleep(5)
#
# post_field = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
# post_field.send_keys(f"Down: {real_down}, Up {real_up}.")
# post_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
# post_button.click()
#
# time.sleep(10)
# print("Post sent")


# IMPLEMENTED WITH CLASSES
#
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        global real_down, real_up
        self.driver.get(SPEED_URL)
        self.driver.maximize_window()
        element = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        element.click()
        time.sleep(45)
        results = self.driver.find_element(By.CLASS_NAME, 'result-container-speed')
        real_down = (float(results.text.split()[2]))
        real_up = (float(results.text.split()[5]))
        print(real_down, real_up)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        login_button = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login_button.click()
        time.sleep(3)

        email_field = self.driver.find_element(By.XPATH, '//input[@name="text"]')
        email_field.send_keys(TWITTER_EMAIL)
        email_submit_button = self.driver.find_element(By.XPATH, '//div[@role="button" and contains(., "Next")]')
        email_submit_button.click()
        time.sleep(10)

        """Note: during login twitter could ask to enter additionally username or requested a password two times"""

        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(TWITTER_PASS)
        time.sleep(2)
        password_submit_button = self.driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
        password_submit_button.click()
        time.sleep(7)

        post_field = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        post_field.send_keys(f"Down: {real_down}, Up {real_up}.")
        post_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        post_button.click()

        time.sleep(10)
        print("Post sent")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if MIN_DOWNLOAD_SPEED > real_down or MIN_UPLOAD_SPEED > real_up:
    bot.tweet_at_provider()
