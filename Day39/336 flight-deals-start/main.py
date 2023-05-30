# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.getSheetyData()
emails = data_manager.getEmails()
flight_search = FlightSearch()

for city in sheet_data:
    if city["iataCode"] == "":
        iataCode = flight_search.get_iata(city=city["city"])
        data_manager.updateIATA(iataCode=iataCode, id=city["id"])

tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")

for city in sheet_data:
    flight_data = flight_search.check_flights(origin_city="LON", destination_city=city["iataCode"], from_time=tomorrow,
                                              to_time=six_months)
    if flight_data.stop_overs > 0:
        is_step_over = True

    if flight_data is None:
        continue

    if flight_data.price < city["lowestPrice"]:
        for user in emails:
            NotificationManager().send_emails(user=user["email"], price=flight_data.price, departure_city=flight_data.origin_city,
                                              departure_airport=flight_data.origin_airport,
                                              arrival_city=flight_data.destination_city,
                                              arrival_airport=flight_data.destination_airport,
                                              inbound_date=flight_data.out_date,
                                              outbound_date=flight_data.return_date)
        # NotificationManager().notify(price=flight_data.price, departure_city=flight_data.origin_city,
        #                              departure_airport=flight_data.origin_airport,
        #                              arrival_city=flight_data.destination_city,
        #                              arrival_airport=flight_data.destination_airport, inbound_date=flight_data.out_date,
        #                              outbound_date=flight_data.return_date)
        # print(flight_data)
        if flight_data.stop_overs > 0:
            is_step_over = True
            # NotificationManager().notify(price=flight_data.price, departure_city=flight_data.origin_city,
            #                              departure_airport=flight_data.origin_airport,
            #                              arrival_city=flight_data.destination_city,
            #                              arrival_airport=flight_data.destination_airport,
            #                              inbound_date=flight_data.out_date,
            #                              outbound_date=flight_data.return_date,
            #                              via_city=flight_data.via_city,
            #                              step_over=flight_data.stop_overs,
            #                              is_step_over=is_step_over
            #                              )
            for user in emails:
                NotificationManager().send_emails(user=user["email"], price=flight_data.price, departure_city=flight_data.origin_city,
                                              departure_airport=flight_data.origin_airport,
                                              arrival_city=flight_data.destination_city,
                                              arrival_airport=flight_data.destination_airport,
                                              inbound_date=flight_data.out_date,
                                              outbound_date=flight_data.return_date,
                                              via_city=flight_data.via_city,
                                              step_over=flight_data.stop_overs,
                                              is_step_over=is_step_over
                                              )