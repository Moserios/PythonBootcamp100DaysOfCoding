import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
TOKEN = os.environ["TOKEN"]
EXERCISE_API = os.environ["EXERCISE_API"]
GOOGLE_SHEET_URL = os.environ["GOOGLE_SHEET_URL"]


# activity
activity_today = input("Which exercises you did today:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

exercise_data = {
     "query": activity_today,
     "gender": ",male",
     "weight_kg": 103,
     "height_cm": 185,
     "age": 34
    }

exercise_response = requests.post(url=EXERCISE_API, json=exercise_data, headers=headers)
data = exercise_response.json()["exercises"][0]
print(data)
activity_name = str(data["name"]).title()
activity_duration = data["duration_min"]
activity_calories = data["nf_calories"]

# saving results to the Google sheet

day_now = dt.datetime.now().day
month_now = dt.datetime.now().month
year_now = dt.datetime.now().year

date_today = f"{day_now}/{month_now}/{year_now}"
time_today = dt.datetime.today().strftime("%X")


google_sheet_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

google_sheet_data = {
    "workout": {
        "date": date_today,
        "time": time_today,
        "exercise": activity_name,
        "duration": activity_duration,
        "calories": activity_calories
    }
}

# google_response = requests.get(url=f"{GOOGLE_SHEET_URL}/2")
google_response = requests.post(url=GOOGLE_SHEET_URL, json=google_sheet_data, headers=google_sheet_headers)
