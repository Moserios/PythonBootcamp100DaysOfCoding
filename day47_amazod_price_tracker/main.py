import requests
from bs4 import BeautifulSoup
import smtplib


EXPECTED_PRICE = 1500
AMAZON_ITEM_URL = "https://www.amazon.com/Dell-Alienware-X17-R2-Laptop/dp/B0B6HY5WBG/ref=sr_1_6?keywords=alienware%2Bx17%2Br2&qid=1699884566&s=pc&sr=1-6&th=1"
MY_SEND_EMAIL = "sergemoserati@gmail.com"
DESTINATION_EMAIL = "moser@gmail.com"
MY_PASS = "ecre vjik cskb nswc"


amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,sr;q=0.6",
}

response = requests.get(url=AMAZON_ITEM_URL, headers=amazon_headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")
prices = soup.find_all(class_="a-offscreen")[0]
prices = prices.getText()[1:].replace(",", "")
current_price = float(prices)

def send_email(price, url):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_SEND_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_SEND_EMAIL, to_addrs=DESTINATION_EMAIL,
                            msg=f"Subject:Price at Amazon reached required level!\n\n "
                                f"Item: {url}\n"
                                f"price: {price}!")


if current_price < EXPECTED_PRICE:
    send_email(current_price, AMAZON_ITEM_URL)



