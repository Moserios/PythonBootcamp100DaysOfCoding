from selenium import webdriver
from selenium.webdriver.common.by import By

# URL = "https://www.amazon.com/Dell-Alienware-Gaming-Laptop-i9-2TB/dp/B0C1XXRDS5/ref=sr_1_2?crid=JTVCGUFON5Y4&keywords=alienware+x17+r2+4k&qid=1699943997&sprefix=alienware+x17+r2+4k%2Caps%2C149&sr=8-2"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)
#
# price = driver.find_element(By.CLASS_NAME, value="a-offscreen")
# # print(price.text)
# print(price.get_attribute("innerHTML"))
# # driver.close()
# driver.quit()

URL = "https://www.python.org/"

driver = webdriver.Chrome()
driver.get(URL)

stored_events = {}
# event1_year = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time/span').text
# event1_date = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time').text

counter = 1
for i in range(0, 5):
    time_url = f"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({counter}) > time"
    event_url = f"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({counter}) > a"
    events_time = driver.find_element(By.CSS_SELECTOR, value=time_url)
    event_time = events_time.get_attribute("datetime").split("T")[0]
    print(event_time) #event1_year., event1_date

    events = driver.find_element(By.CSS_SELECTOR, value=event_url)
    event = events.text
    print(event) #event1_year., event1_date
    
    stored_events[i] = {"time": event_time, "name": event}

    # stored_events[i]["time"] = event_time
    # stored_events[i]["name"] = event
    counter += 1
print(stored_events)