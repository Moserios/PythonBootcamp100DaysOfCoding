# import smtplib
#
# my_email = "sergemoseratti@gmail.com"
# my_password = "ecre vjik cskb nswc"
# recipient_email = "sergemoseratti@yahoo.com"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=recipient_email,
#     msg="Subject:Hello.\n\n It's a test message")
# connection.close()

#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=recipient_email,
#         msg="Subject:Hello.\n\n It's a test message")


################ DATETIME MODULE #################

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# weekday = now.weekday()
# print(now)
# print(year)
# print(weekday)
# DOB = dt.datetime(year=1979, month=10, day=15, hour=22)
# print(DOB)

########################################## SENT RANDOM QUOTE EVERY MONDAY #######################
#
# import smtplib
# import datetime as dt
# import random
# weekday = dt.datetime.now().weekday()
#
# my_email = "sergemoseratti@gmail.com"
# my_password = "ecre vjik cskb nswc"
# recipient_email = "sergemoseratti@yahoo.com"
#
# def send_quote():
#     with open("quotes.txt", "r") as quotes_file:
#         data = quotes_file.read()
#     quotes = data.split("\n")
#     random_quote = random.choice(quotes)
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=recipient_email,
#             msg=f"Subject:Monday's motivational quote.\n\n {random_quote}")
#
# if weekday == 0:
#     send_quote()

################## BIRTHDAYS CONGRATS AUTO EMAIL ####################

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

import smtplib
import pandas
import datetime as dt
import random

my_email = "sergemoseratti@gmail.com"
my_password = "ecre vjik cskb nswc"

def send_congratulation(recipient_email, birthday_boy_name, letter_text):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,msg=f"Subject:Happy Birthday, {birthday_boy_name}!\n\n{letter_text}")


month = dt.datetime.now().month
day = dt.datetime.now().day
birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")

with open("letter_templates/letter_1.txt", 'r') as template_file1:
    template1 = template_file1.read()
with open("letter_templates/letter_2.txt", 'r') as template_file2:
    template2 = template_file2.read()
with open("letter_templates/letter_3.txt", 'r') as template_file3:
    template3 = template_file3.read()
letter_templates = [template1, template2, template3]

index = 0
for row in birthdays:
    record_name = birthdays[index]["name"]
    record_email = birthdays[index]["email"]
    record_month = birthdays[index]["month"]
    record_day = birthdays[index]["day"]

    if record_day == day and record_month == month:
        letter_template = random.choice(letter_templates)
        letter = letter_template.replace('[NAME]', record_name)
        send_congratulation(recipient_email = record_email, birthday_boy_name = record_name, letter_text = letter)
    index += 1

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



