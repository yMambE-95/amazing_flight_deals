from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/398e8df0e3399652af0938c7a0adb26c/myFlightDeals/prices"


class DataManager:
    # this class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            # print(response.text)
