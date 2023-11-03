from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/bc34e9281854b82a6cec777041567a41/flightDeals/prices'
SHEET_USERS_ENDPOINT = 'https://api.sheety.co/bc34e9281854b82a6cec777041567a41/flightDeals/user'
FLIGHT_LIST_TOKEN = "a236ea0f-25cd-428e-bf01-6b5705b2412a"

flight_list_headers = {
    "Authorization": f"Bearer {FLIGHT_LIST_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=flight_list_headers)
        data = response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, headers=flight_list_headers)
        data = response.json()
        # pprint(data)
        self.customer_data = data["user"]
        return self.customer_data
