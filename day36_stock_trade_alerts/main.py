import requests
import datetime as dt
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = "TQ----------"
STOCK_UP_ICON = "🔺"
STOCK_DOWN_ICON = "🔻"
account_sid = "ACa54-----------"
auth_token = "491ba9-------"

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "b5f--------------------"


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour

time_now = hour
date_today = f"{year}-{month}-{day}"
date_yesterday = f"{year}-{month}-{day-1}"
date_before_yesterday = f"{year}-{month}-{day-2}"
date_3_days_ago = f"{year}-{month}-{day-3}"


# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=full&apikey=TQ4K8P1S3HBVEZWV

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "full",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_URL, params=parameters_stock)
response.raise_for_status()
data_stock = response.json()

daily_value1 = float(data_stock["Time Series (Daily)"][date_yesterday]["1. open"])
daily_value2 = float(data_stock["Time Series (Daily)"][date_before_yesterday]["1. open"])

daily_movement = daily_value1-daily_value2
percent_daily_movement = round((100 * daily_value1 / daily_value2) - 100, 2)


parameters_news = {
    "q": "tesla",
    "from": date_yesterday,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}
# https://newsapi.org/v2/everything?q=tesla&from=2023-09-20&sortBy=publishedAt&apiKey=b5f304c64754404c9ebd57170c59935f
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}


response = requests.get(NEWS_URL, params=parameters_news)
response.raise_for_status()
data_news = response.json()
articles = data_news["articles"][:3]
index = 0
for article in articles:
    if daily_movement > 0:
        trend = STOCK_UP_ICON
    else:
        trend = STOCK_DOWN_ICON

    news_title = articles[index]["title"]
    # news_description = articles[index]["description"]
    news_url = articles[index]["url"]
    text_message = f"{STOCK}: {trend}{percent_daily_movement}%\nHeadline: {news_title}\nURL: {news_url}"

    client = Client(account_sid, auth_token)  # , http_client=proxy_client
    message = client.messages \
        .create(
        from_='Your virtual phone number',
        body=text_message,
        to='your verified phone number'
    )
    index += 1


######################### bootcamp solution ##########################
#
# import requests
# from twilio.rest import Client
#
# VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
# VERIFIED_NUMBER = "your own phone number verified with Twilio"
#
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#
# STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
# NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
# TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
# TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
#
# ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# #Get yesterday's closing stock price
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": STOCK_API_KEY,
# }
#
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()["Time Series (Daily)"]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)
#
# #Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)
#
# #Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# up_down = None
# if difference > 0:
#     up_down = "🔺"
# else:
#     up_down = "🔻"
#
# #Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)
#
#
#     ## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
# #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# #If difference percentage is greater than 5 then print("Get News").
# if abs(diff_percent) > 1:
#     news_params = {
#         "apiKey": NEWS_API_KEY,
#         "qInTitle": COMPANY_NAME,
#     }
#
#     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     articles = news_response.json()["articles"]
#
#     #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
#     three_articles = articles[:3]
#     print(three_articles)
#
#     ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.
#
#     #Create a new list of the first 3 article's headline and description using list comprehension.
#     formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#     print(formatted_articles)
#     #Send each article as a separate message via Twilio.
#     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
#     #TODO 8. - Send each article as a separate message via Twilio.
#     for article in formatted_articles:
#         message = client.messages.create(
#             body=article,
#             from_=VIRTUAL_TWILIO_NUMBER,
#             to=VERIFIED_NUMBER
#         )
