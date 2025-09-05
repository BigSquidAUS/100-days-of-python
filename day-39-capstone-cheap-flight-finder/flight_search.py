import os
import requests
import datetime as dt
from dateutil.relativedelta import relativedelta


AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
AMADEUS_BASE_URL = "https://test.api.amadeus.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.from_date = self.get_dates()[0] # Today's date (Format: YYYY-MM-DD)
        self.to_date = self.get_dates()[1] # Today's date plus 6 months. (Format: YYYY-MM-DD)
        self.request_header = self.authenticate()

    def authenticate(self): # Returns an access token in the form on an authorisation header.
        auth_headers = { "Content-Type": "application/x-www-form-urlencoded" }
        auth_body = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET
        }
        auth_response = requests.post(f"{AMADEUS_BASE_URL}/v1/security/oauth2/token", data=auth_body,
                                      headers=auth_headers)

        return {"Authorization": f"Bearer {auth_response.json()["access_token"]}"}

    def get_dates(self):
        self.dt_now = dt.datetime.now().date()  # .date() gets date only, not time.
        self.from_date = self.dt_now + relativedelta(days=1) #Add 1 day to today's date. ie (Tomorrow's date).
        self.from_date = self.dt_now.strftime("%Y-%m-%d")  # YYYY-MM-DD
        self.to_date = self.dt_now + relativedelta(months=6)
        return [self.from_date,self.to_date]

    def search_flights(self,destination):
        request_data = {
            "originLocationCode": "ADL",
            "destinationLocationCode":destination,
            "departureDate": self.from_date,
            "returnDate": self.to_date,
            "adults": "1",
            "currencyCode": "AUD",
            "nonStop": "false",
        }
        response = requests.get(f"{AMADEUS_BASE_URL}/v2/shopping/flight-offers",request_data,headers=self.request_header)
        flights_result = response.json()
        #print(response.text)
        for entry in flights_result["data"]:
            print(f"${entry["price"]["grandTotal"]} {entry["price"]["currency"]}")


    def city_search(self, search_term:str): #Searches for city and returns it's IATA Code
        request_data = {
            "keyword" : search_term,
            "max" : "1",
        }
        response = requests.get(f"{AMADEUS_BASE_URL}/v1/reference-data/locations/cities",params=request_data,headers=self.request_header)
        city_result = response.json()
        try:
            code = city_result["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError:  No airport code found for {search_term}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {search_term}")
            return "Not Found"
        return code