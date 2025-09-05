#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dateutil.relativedelta import relativedelta

import data_manager
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
import notification_manager

fs = FlightSearch()
fd = FlightData()
dm = DataManager()

#Populate the spreadsheet with IATA Codes
for value in dm.sheet_data["prices"]:
    if not len(value["iataCode"]): # Checking length of the iataCode
     #print(value)
     iata_code = fs.city_search(value["city"])
     #print(f"Adding IATA Code ({iata_code}) for {value["city"]}")
     dm.edit_row(str(value["id"]),"iataCode",iata_code)
    else:
        pass
        #print(f"{value["city"]}'s IATA code is {value["iataCode"]}")

fs.search_flights("SFO")