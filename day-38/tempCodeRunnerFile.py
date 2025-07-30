import requests
from datetime import datetime

APP_ID = "43da93d3"
API_KEY = "7caab417c262fb011bda2de2e6139705"
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

    response = requests.post(SHEETY_URL,json=exercise_config, auth=("sennn", "12345!"))
    print(response.text)


