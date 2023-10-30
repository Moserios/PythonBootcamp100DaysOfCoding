import requests
from pprint import pprint
from data_manager import *
from flight_search import *


flights_list_response = requests.get(url=FLIGHTS_LIST_URL, headers=flight_list_headers)
sheet_data = flights_list_response.json()["prices"]
pprint(sheet_data)

iata_codes = []
ticket_prices = []
index = 0
while index < len(sheet_data):
    iata_code = sheet_data[index]["iataCode"]
    ticket_prices.append(sheet_data[index]["lowestPrice"])
    if len(iata_code) < 3:
        response = FlightSearch.iata_code(city_name=sheet_data[index]["city"])
        sheet_data[index]['iataCode'] = response
        iata_code = response
    iata_codes.append(iata_code)
    index += 1
DataManager.update_iata_codes(sheet_data)

FlightSearch.check_flight(list_of_city_codes=iata_codes, prices=ticket_prices)
