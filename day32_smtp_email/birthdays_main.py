import smtplib
import pandas
import datetime as dt
import random

my_email = "serge@gmail.com"
my_password = "ecre vjik cskb nswe"

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

