# API (Application Programming Interface)
import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
# 1XX -> Hold On
# 2XX -> Success
# 3XX -> Go away , No Permission
# 4XX -> You Screwed Up
# 5XX -> I Screwed Up

# API  Parameters
MY_LAT = 1.135792
MY_LANG = 104.035233
parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LANG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)