import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 1. TODO: create a new form in Google Forms. https://docs.google.com/forms/
# Done

# 2. TODO: Add 3 questions to the form, make all questions "short-answer":
# Address
# Price per month
# Link
# Save link to the form!
# Done

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdC7-3aE-ltZOiGBaEKuK6-gfdLjLPAF-qLuqrmNVPAn0gDKA/viewform?usp=sf_link'
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'

# 3. TODO: Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address
# https://appbrewery.github.io/Zillow-Clone/

response = requests.get(ZILLOW_URL).text
parsed_data = BeautifulSoup(response, 'html.parser')


# 4. TODO: Create a list of addresses for all the listings you scraped.
address_records = parsed_data.css.select(".StyledPropertyCardDataArea-anchor")
all_addresses = []
for address in address_records:
    cleared_address = address.get_text().strip()
    all_addresses.append(cleared_address)



# 5. TODO: Create a list of prices for all the listings you scraped.
price_records = parsed_data.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
all_prices = []
for price in price_records:
    cleared_price = price.get_text().replace(',', '').split('+')[0].split('/')[0]
    all_prices.append(cleared_price)


# 6. TODO: Create a list of links for all the listings you scraped
link_records = parsed_data.css.select(".StyledPropertyCardDataArea-anchor")
all_links = []

for link in link_records:
    cleared_link = link.get('href')
    all_links.append(cleared_link)


# 7. TODO: Use Selenium to fill in the form created above.
#  Each listing should have its price/address/link added to the form.
#  Fill in a new form for each new listing.
driver = webdriver.Chrome()
driver.get(FORM_URL)
time.sleep(2)

for i in range(0, len(all_addresses)):
    address_field = driver.find_element(By.XPATH, "//input[contains(@class, 'whsOnd') and contains(@aria-labelledby, 'i1')]")
    address_field.send_keys(all_addresses[i])

    price_field = driver.find_element(By.XPATH, "//input[contains(@class, 'whsOnd') and contains(@aria-labelledby, 'i5')]")
    price_field.send_keys(all_prices[i])

    link_field = driver.find_element(By.XPATH, "//input[contains(@class, 'whsOnd') and contains(@aria-labelledby, 'i9')]")
    link_field.send_keys(all_links[i])

    submit_form = driver.find_element(By.XPATH, "//div[contains(@role, 'button') and contains (@jsname, 'M2UYVd')]")
    submit_form.click()
    time.sleep(0.5)

    # another_form = driver.find_element(By.LINK_TEXT, 'Submit another response')
    # another_form.click()
    driver.get(FORM_URL)
    time.sleep(0.5)

