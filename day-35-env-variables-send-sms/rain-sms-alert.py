import os
import requests

weather_api_key = os.getenv("OPENWEATHER_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_lat = os.getenv("MY_LAT")
my_long = os.getenv("MY_LONG")

parameters = {
    "lat" : my_lat,
    "lon" : my_long,
    "cnt" : 4,
    "appid" : weather_api_key,
}

request = requests.get(weather_endpoint,params=parameters)
request.raise_for_status()
data = request.json()

will_rain = False

for forecast in data["list"]:
    #Weather ID's less than 700 indicate rain. https://openweathermap.org/weather-conditions
    #print(forecast['weather'][0]['id'])
    weather_id = int(forecast['weather'][0]['id'])
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("It will rain in the next 12 hours.")
else:
    print("No rain detected for next 12 hours.")