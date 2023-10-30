import requests
from notification_manager import *
import datetime as dt

FLIGHT_API_KEY = "Nf8NjB-mm7BYSt-i0sifBsBnCGJsTRhT-2"
FLIGHT_LOCATIONS_URL = "https://api.tequila.kiwi.com/locations/query"
FLIGHTS_SEARCH_URL = "https://api.tequila.kiwi.com/v2/search"

headers = {
    "apikey": FLIGHT_API_KEY,
    "accept": "application/json"
}

class FlightSearch:
    def __init__(self):
        pass

    def iata_code(city_name):

        FLIGHT_LOCATIONS_PARAMS = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": "1",
            "active_only": "true"
        }

        response = requests.get(url=FLIGHT_LOCATIONS_URL, headers=headers, params=FLIGHT_LOCATIONS_PARAMS)
        iata_code = response.json()['locations'][0]["code"]
        return iata_code


    def check_flight(list_of_city_codes, prices):
        date = dt.datetime.now()
        day_now = date.day
        month_now = date.month
        year_now = date.year
        date_now = dt.datetime(day=day_now, month=month_now, year=year_now)
        date_now_formatted = date_now.strftime("%d/%m/%Y")
        date_future = dt.datetime.now() + dt.timedelta(days=178)
        date_future_formatted = date_future.strftime("%d/%m/%Y")


        flight_from = list_of_city_codes[0]

        for city in range(1, len(list_of_city_codes)):
            flight_to = list_of_city_codes[city]

            FLIGHT_SEARCH_PARAMS = {
                "fly_from": flight_from,
                "fly_to": flight_to,
                "date_from": date_now_formatted,
                "date_to": date_future_formatted,
                "one_for_city": "1",
                "one_per_date": "1",
                "adults": "1",
                "selected_cabins": "M",
                "adult_hold_bag": 1,
                "adult_hand_bag": 1,
                "only_working_days": "false",
                "only_weekends": "false",
                "partner_market": "us",
                "max_stopovers": 2,
                "max_sector_stopovers": 2,
                "vehicle_type": "aircraft"
            }

            response = requests.get(url=FLIGHTS_SEARCH_URL, headers=headers, params=FLIGHT_SEARCH_PARAMS)
            response_search_data = response.json()['data']

            min_price = 0
            min_price_date = None

            for record in response_search_data:
                if min_price == 0:
                    min_price = round(record["price"])
                    min_price_date = (record["local_departure"]).split("T")[0]
                if record["price"] < min_price:
                    min_price = round(record["price"])
                    min_price_date = (record["local_departure"]).split("T")[0]

            if min_price < prices[city]:
                NotificationManager.send_message(flight_from, flight_to, min_price, min_price_date)
