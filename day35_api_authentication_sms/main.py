################## Rain notification service (uses SMS) #################

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "ACa54aecca42ca482065a2b352deb4556a"
auth_token = "491ba9d2b027492bbed6c156b59c42d1"
API_KEY = "c5df37fe2595728ba24ead4b91cf0a43"
MY_LAT = 44.786568
MY_LON = 20.448921
URL = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=URL, params=parameters)
# print(response)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
# print(weather_data['hourly'])

umbrella_codes = []
nearest_12_hours = []
hour = 0

while hour < 12:
    code = weather_data['hourly'][hour]["weather"][0]["id"]
    # print(code)
    nearest_12_hours.append(code)
    hour += 1

print(nearest_12_hours)

for index in nearest_12_hours:
    if index < 700:
        umbrella_codes.append(index)


if len(umbrella_codes) > 0:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        from_='+122442315945',
        body="Hey. It's Sergey Molchun's service! Take an umbrella, expecting rain during next 12 hours.",
        to='+3812345678'
    )
    print(message.status)


##################### Birthday congratulator ###################
#
# import smtplib
# import pandas
# import datetime as dt
# import random
#
# my_email = "serge@gmail.com"
# my_password = "ecre vjik cskb nswc"
#
# def send_congratulation(recipient_email, birthday_boy_name, letter_text):
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email, to_addrs=recipient_email,msg=f"Subject:Happy Birthday, {birthday_boy_name}!\n\n{letter_text}")
#
#
# month = dt.datetime.now().month
# day = dt.datetime.now().day
# birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
#
# with open("letter_templates/letter_1.txt", 'r') as template_file1:
#     template1 = template_file1.read()
# with open("letter_templates/letter_2.txt", 'r') as template_file2:
#     template2 = template_file2.read()
# with open("letter_templates/letter_3.txt", 'r') as template_file3:
#     template3 = template_file3.read()
# letter_templates = [template1, template2, template3]
#
# index = 0
# for row in birthdays:
#     record_name = birthdays[index]["name"]
#     record_email = birthdays[index]["email"]
#     record_month = birthdays[index]["month"]
#     record_day = birthdays[index]["day"]
#
#     if record_day == day and record_month == month:
#         letter_template = random.choice(letter_templates)
#         letter = letter_template.replace('[NAME]', record_name)
#         send_congratulation(recipient_email = record_email, birthday_boy_name = record_name, letter_text = letter)
#     index += 1
