import requests
from datetime import datetime

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/9127e9ba0da22990287cac27aade73f3/workoutTracker/sheet1"

API_Key = "f7dd43eca67dbdc574eb08f3c8aded88"
APP_ID = "5a37f3e8"
exercises_list = []
calories_list = []
duration_list = []

user_input = input("Tell Me What Exercise You Did : ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_Key,
    "Content-Type": "application/json",
}

exercise_data = {
    "query": user_input,
}

response = requests.post(url=API_ENDPOINT, json=exercise_data, headers=headers)
response.raise_for_status()
for exercise in response.json()["exercises"]:
    exercises_list.append(exercise["name"])
    calories_list.append(exercise["nf_calories"])
    duration_list.append(exercise["duration_min"])

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer Secret",
}

print(time)
for i in range(len(exercises_list)):
    workout = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercises_list[i],
            "duration": duration_list[i],
            "calories": calories_list[i],
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=workout, headers=sheety_header)
    print(sheety_response.json())
