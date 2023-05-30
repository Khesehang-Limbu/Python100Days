from pprint import pprint

import requests
from flight_data import FlightData

FLIGHTY_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "O0R46a8uGn_rWpSxkWhVMD-0Pv8d_j4x"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata(self, city):
        FLIGHTY_IATA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

        # Getting IATA codes
        search_params = {
            "term": city,
        }
        headers = {
            "accept": "application/json",
            "apikey": API_KEY,
        }
        iata_response = requests.get(url=FLIGHTY_IATA_SEARCH_ENDPOINT, params=search_params, headers=headers).json()
        return iata_response["locations"][0]["code"]


    def check_flights(self, origin_city, destination_city, from_time, to_time):
        # Searching for flights
        headers = {
            "accept": "application/json",
            "apikey": API_KEY,
        }

        flight_params = {
            "fly_from": origin_city,
            "date_from": from_time,
            "date_to": to_time,
            "fly_to": destination_city,
            "curr": "GBP",
            "vehicle_type": "aircraft",
            "sort": "price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        flight_search_response = \
            requests.get(url=FLIGHTY_SEARCH_ENDPOINT, params=flight_params, headers=headers).json()

        try:
            data = flight_search_response["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            flight_params["max_stopovers"] = 2
            pprint(flight_params)
            flight_search_response = requests.get(url=FLIGHTY_SEARCH_ENDPOINT, params=flight_params, headers=headers).json()

            pprint(flight_search_response)

            data = flight_search_response["data"][0]
            via_city = data["route"][0]["cityTo"]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["cityCodeTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                via_city=via_city,
                stop_overs=2
            )
            return flight_data

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data
