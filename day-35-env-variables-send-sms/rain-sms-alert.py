import os
import requests
from twilio.rest import Client

weather_api_key = os.getenv("OPENWEATHER_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_lat = os.getenv("MY_LAT")
my_long = os.getenv("MY_LONG")

weather_parameters = {
    "lat" : my_lat,
    "lon" : my_long,
    "cnt" : 4,
    "appid" : weather_api_key,
}

twilio_sid = os.getenv("TWILIO_SID")
twilio_auth_token = os.getenv("TWILIO_AUTHTOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NO")
twilio_recipient_number = os.getenv("MY_PHONE_NO")

twilio_parameters = {
    "account_sid" : twilio_sid,
    "auth_token" : twilio_auth_token,
}

twilio_client = Client(twilio_sid,twilio_auth_token)

request = requests.get(weather_endpoint,params=weather_parameters)
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
    message = twilio_client.messages.create(
        from_=twilio_phone_number,
        body='Uh oh! It\'s gon\' rain!\n(In the next 12-hours)',
        to=twilio_recipient_number,
    )

    print(message.sid)

else:
    print("No rain detected for next 12 hours.")