import os
import requests
from datetime import datetime

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 39

exercise_text = input("Tell me which exercises you did: ")

#https://developer.nutritionix.com/admin
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
APP_USER = os.getenv("APP_USER")
auth_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
auth_headers = {
    'Content-Type' : 'application/json',
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "0",
}
query_data = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}
response = requests.post(auth_endpoint,json=query_data,headers=auth_headers)
result = response.json()
print(result)

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ADD_ROW = "https://api.sheety.co/2a052476d154c1149b5186b24be3c7d4/workoutTracking/workouts"
sheety_headers = {"Authorization" : f"Bearer {SHEETY_TOKEN}"}
for exercise in result['exercises']:
    sheety_query = {
        "workout": {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories']
        }
    }

    sheet_response = requests.post(SHEETY_ADD_ROW, json=sheety_query, headers=sheety_headers)
    print(sheet_response.text)