import os
import requests

SHEETY_EP = os.getenv("SHEETY_END_POINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
sheety_headers = {
    "Authorization" : f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(SHEETY_EP, headers=sheety_headers)
        return response.json()

    def edit_row(self, object_id, row_to_edit, new_value):
        sheety_data = {
            "price": {
                str(row_to_edit): str(new_value)
            }
        }
        response = requests.put(f"{SHEETY_EP}/{object_id}", json=sheety_data, headers=sheety_headers)
        return response