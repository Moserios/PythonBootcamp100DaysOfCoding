import requests

FLIGHTS_LIST_URL = "https://api.sheety.co/bc34e9281854b82a6cec777041567a41/flightDeals/prices"#os.environ['FLIGHTS_LIST_URL'] #
FLIGHT_LIST_TOKEN = "a236ea0f-25cd-428e-bf01-6b5705b2412b"

flight_list_headers = {
    "Authorization": f"Bearer {FLIGHT_LIST_TOKEN}"
}

class DataManager:
    def __init__(self):
        pass

    def update_iata_codes(sheet_data):
        for location in sheet_data:
            row = location['id']
            iata_code = location['iataCode']
            update_data = {"price": {'iataCode': iata_code},}
            flights_list_update_response = requests.put(url=f"{FLIGHTS_LIST_URL}/{row}", headers=flight_list_headers, json=update_data)
            print(flights_list_update_response.status_code)