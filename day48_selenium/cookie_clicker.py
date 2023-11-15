import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)
time.sleep(5)
# actionChains = ActionChains(driver)
cookie = driver.find_element(By.ID, "bigCookie")

def run_game():
    try:
        while True:
            # cookie.click()
            # actionChains.move_to_element(cookie).click().perform()
            cookie.click()
            time.sleep(0.025)
    except:
        print("Something is wrong. The loop is broken. Waiting 30 seconds for retry!")
        time.sleep(30)
    finally:
        print("Retrying continue the game.")
        run_game()
run_game()


print("Out of the scope. Starting the game final time.")
run_game()
