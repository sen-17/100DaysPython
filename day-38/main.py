import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
MY_USERNAME = os.getenv("MY_USERNAME")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SHEETY_URL = "https://api.sheety.co/e538d1d0cd7df47a8de3f3f45553ecdf/workoutTrackerPython/workouts"
URL = "https://trackapi.nutritionix.com"


headers = {
    "x-app-id" : APP_ID,
    "x-app-key": API_KEY
}

user_exercise = input("What exercise did you do? ")

query_config = {
    "query" : user_exercise
}

response = requests.post(f'{URL}/v2/natural/exercise',json=query_config, headers=headers)
data = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    exercise_config = {
        "workout" : {
            "date": date,
            "time" : time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    response = requests.post(SHEETY_URL,json=exercise_config, auth=(MY_USERNAME, MY_PASSWORD))
    print(response.text)


