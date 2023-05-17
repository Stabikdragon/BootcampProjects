# API url ref: https://developer.nutritionix.com/
# Goole sheet ref:
import requests
import datetime


API_ID = "8f299132"
API_KEY = "059ff7f9a625eaa5b925dcf7ac0f9e8f"
SHEET_ENDPOINT ="https://api.sheety.co/47699632e90ecb34eb3ac6e574b1f8ba/myWorkouts/workouts"

HEADERS = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}
params={
 "query": "run 3 minutes"
}
today = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().isoformat()[:8]

response2 = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=params,headers=HEADERS)
data = response2.json()["exercises"]
exercise_data = data[0]['name']
duration_data = data[0]['duration_min']
calories_data = data[0]['nf_calories']

workout_params ={
    "workout":{
        "exercise": exercise_data,
        "duration": duration_data,
        "calories": calories_data,
        "date": today,
        "time": time
    }
}

response = requests.post(url=SHEET_ENDPOINT , json=workout_params)
print(time)

# response = requests.get(url="https://api.sheety.co/47699632e90ecb34eb3ac6e574b1f8ba/myWorkouts/workouts")
# print(response.json()
