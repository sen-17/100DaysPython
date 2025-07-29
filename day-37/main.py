import requests
from datetime import datetime

USERNAME = "sennnnnnnn"
TOKEN = "fsldkfl123123181029"
GRAPH_ID = "graph176"

pixela_endpoint = "https://pixe.la/v1/users"

# ------------------------------------------ SETTING USERNAME AND TOKEN ------------------------------------------
params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url = pixela_endpoint, json=params)
# print(response.text)

# ------------------------------------------ CREATE GRAPH ------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Commit",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text) 
# datetime(year=2025, month=7, day=22) # yesterday

# ------------------------------------------ ADD PIXEL ------------------------------------------
today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_config = {
    "date": date,
    "quantity": "2",
}

# add_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
# response = requests.post(url=add_pixel_endpoint, json = pixel_config, headers=headers)
# print(response.text)

# ------------------------------------------ UPDATE PIXEL ------------------------------------------
update_pixel_config = {
    "quantity" : "9"
}
update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
# response = requests.put(update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# ------------------------------------------ DELETE PIXEL ------------------------------------------
# response = requests.delete(update_pixel_config, headers=headers)

