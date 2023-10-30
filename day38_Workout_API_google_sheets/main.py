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


############## BOOTCAMP SOLUTION #################
#
# import requests
# from datetime import datetime
# import os
#
# # Your personal data. Used by Nutritionix to calculate calories.
# GENDER = "male"
# WEIGHT_KG = 84
# HEIGHT_CM = 180
# AGE = 32
#
# # Nutritionix APP ID and API Key. Actual values are stored as environment variables.
# APP_ID = os.environ["ENV_NIX_APP_ID"]
# API_KEY = os.environ["ENV_NIX_API_KEY"]
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
#
# exercise_text = input("Tell me which exercises you did: ")
#
# # Nutritionix API Call
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }
#
# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
#
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(f"Nutritionix API call: \n {result} \n")
#
# # Adding date and time
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
#
# # Sheety Project API. Check your Google sheet name and Sheety endpoint
# GOOGLE_SHEET_NAME = "workout"
# sheet_endpoint = os.environ[
#     "ENV_SHEETY_ENDPOINT"]
#
# # Sheety API Call & Authentication
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         GOOGLE_SHEET_NAME: {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
#     # Sheety Authentication Option 1: No Auth
#     """
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#     """
#
#     # Sheety Authentication Option 2: Basic Auth
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         auth=(
#             os.environ["ENV_SHEETY_USERNAME"],
#             os.environ["ENV_SHEETY_PASSWORD"],
#         )
#     )
#
#     # Sheety Authentication Option 3: Bearer Token
#     """
#     bearer_headers = {
#         "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
#     }
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         headers=bearer_headers
#     )
#     """
#     print(f"Sheety Response: \n {sheet_response.text}")
