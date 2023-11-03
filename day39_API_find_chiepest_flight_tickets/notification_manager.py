import smtplib

my_email = "sergemoseratti@gmail.com"
recipient_email = "moserturbo@gmail.com"
my_password = "ecre vjik cskb nswd"
class NotificationManager():
    def __init__(self):
        pass

    def send_message(flight_from, flight_to, price, date):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                                msg=f"Subject:Cheap flight {flight_from}:{flight_to}!\n\n Price for flight {flight_from}:{flight_to} is {price}Eur on {date}")







