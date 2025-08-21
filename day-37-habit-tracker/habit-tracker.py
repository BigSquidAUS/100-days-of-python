import os
import requests
import datetime as dt

#https://pixe.la/v1/users/bigsquidaus/graphs/graph01.html

#Create new Pixela user
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_user = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#response = requests.post(pixela_endpoint,json=pixela_user)

#Create new graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id" : "graph01",
#     "name" : "Coding Graph",
#     "unit" : "Commits",
#     "type" : "float",
#     "color" : "kuro",
#     "timezone" : "Australia/Adelaide"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)

#Create new pixel
now = dt.datetime.now()
today = now.strftime("%Y%m%d")
GRAPH_ID = "graph01"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN,
}
pixel_config = {
    "date":today,
    "quantity":"5",
}
#response = requests.post(pixel_endpoint,json=pixel_config,headers=headers) #POST request creates a new pixel.

#Edit existing pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#response = requests.put(pixel_endpoint,json=pixel_config,headers=headers) #PUT request updates existing pixel.

#Delete a pixel
response = requests.delete(pixel_endpoint,headers=headers) #DELETE request deletes pixel at specified end-point.

print(response.text)