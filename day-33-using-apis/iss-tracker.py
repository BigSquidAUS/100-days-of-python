import requests
import smtplib
import os
from datetime import datetime

def send_alert():
    #Make sure SMTP details are set in your Python Environmental Variables.
    host = os.getenv("SMTP_SERVER")
    user_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PW")
    recipient = "ben.scholz86@gmail.com"
    msg = "Subject: ISS is visible\n\n"
    msg += "Look Up."

    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()
        connection.login(user_email,password)
        connection.sendmail(user_email,recipient,msg)

def is_dark(sunset_hr, sunrise_hr, current_hr):
    if current_hr >= sunset_hr or current_hr < sunrise_hr:
        return True
    else:
        return False

def iss_in_vicinity(iss_lat, iss_long, my_lat, my_long, margin):
    lat_range = False
    long_range = False

    # Check latitude range.
    if (my_lat - margin) <= iss_lat <= (my_lat + margin):
        lat_range = True
        print("ISS within lat range")
    # Check longitude range
    if (my_long - margin) <= iss_long <= (my_long + margin):
        long_range = True
        print("ISS within long range")

    if lat_range and long_range:
        print("ISS in range.")
        return True
    else:
        return False

#--------TIME | SUNRISE | SUNSET | Data-----------#
my_latitude = float(os.getenv("MY_LAT"))
my_longitude = float(os.getenv("MY_LONG"))
error_margin = 5 #Degrees of error when calculating ISS overhead. eg + or - 5 degrees.

parameters = {
# Keys must match those given in documentation. https://sunrise-sunset.org/api
    "lat":my_latitude,
    "lng":my_longitude,
    "tzid":"Australia/Adelaide",
    "formatted":0, # Turns off time formatting.
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = datetime.now()

print(sunrise)
print(sunset)

sunrise = sunrise.split("T")[1].split(":")
sunset = sunset.split("T")[1].split(":")
#Splits up the data in the API response, firstly to get the time, secondly to split the time up.

sunrise_hour = int(sunrise[0])
sunset_hour = int(sunset[0])
now_hour = int(time_now.hour)
#Get only the hour from the split-up response above.
print(f"Sunrise Hour: {sunrise_hour}")
print(f"Sunset Hour: {sunset_hour}")
print(f"Now Hour: {now_hour}")

#------------ISS DATA------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

print(f"ISS Latitude: {iss_lat}")
print(f"ISS Longitude: {iss_long}")

#Determine if dark.
if is_dark(sunset_hour,sunrise_hour,now_hour):
    print("It's dark")
else:
    print("It's not dark")

#Function if ISS within your lat/long given error margin
if iss_in_vicinity(iss_lat,iss_long,my_latitude,my_longitude,error_margin):
    print("ISS within visible range")
else:
    print("ISS out of visible range")

if is_dark(sunset_hour,sunrise_hour,now_hour) and iss_in_vicinity(iss_lat,iss_long,my_latitude,my_longitude,error_margin):
    send_alert()