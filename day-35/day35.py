import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

params = {
    "lat": "1.085728",
    "lon": "104.012414",
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
# print(data["list"][0]["weather"][0]["id"])
weather_id = [item["weather"][0]["id"] for item in data["list"]]

will_rain = False
for id in weather_id:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_="whatsapp:+14155238886",
        to="whatsapp:+6281378195895"
    )
    print(message.status)
