# from tkinter import *
# import requests
#
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest/")
#     if response.status_code != 200:
#         response.raise_for_status()
#     else:
#         data = response.json()
#         canvas.itemconfig(quote_text, text=data['quote'])
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()

############ Longitute Latitude API ########### https://api.sunrise-sunset.org/

# ### BELGRADE
# import requests
# import datetime as dt
#
# MY_LAT = 44.786568
# MY_LONG = 20.448921
# US_TIME_FORMAT = 0
#
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": US_TIME_FORMAT,
# }
#
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# time_now = dt.datetime.now()
# data = response.json()
# sunrise = data["results"]['sunrise'].split("T")[1].split(":")[0]
# sunset = data["results"]['sunset'].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)
# print(time_now.hour)



################## ISS position app #################


import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "sergemoseratti@gmail.com"
MY_PASS = "ecre vjik cskb nswe"
RECIPIENT_EMAIL = "moserturbo@gmail.com"


MY_LAT = int(44.786568) # Your latitude
MY_LONG = int(20.448921) # Your longitude
US_TIME_FORMAT = 0

valid_lat = range(MY_LAT - 5, MY_LAT + 5)
valid_long = range(MY_LONG - 5, MY_LONG + 5)

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = int(float(data["iss_position"]["latitude"]))
    iss_longitude = int(float(data["iss_position"]["longitude"]))

    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude in valid_lat and iss_longitude in valid_long:
        print("First IF")
        # or iss_latitude >= MY_LAT in range(-5, 5) and iss_longitude <= MY_LONG in range(5) or iss_longitude >= MY_LONG in range(5)
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": US_TIME_FORMAT,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour
        valid_evening_time = range(sunset, 24)
        valid_morning_time = range(0, sunrise)

        if time_now in valid_evening_time or time_now in valid_morning_time:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECIPIENT_EMAIL,
                    msg=f"Subject: ISS is near your location.\n\n ISS is near you:\nLatitude:{iss_latitude}\nLongitude:{iss_longitude}")

    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



