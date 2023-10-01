import os

import pandas
import requests
from twilio.rest import Client
account_sid = 'AC4d0c2df6430e45223accba1bd539c697'
auth_token = 'f77d3f973c4dc5bdb9d939819ccc8afa'






api_key = "ce59a617ee2fd0fc676023b8f416454f"

LAT = 37.368832
LONG = -122.036346

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()


weather_slice = weather_data["list"][:4]
# weather_data = response.json()["list"][0]["weather"][0]["description"]
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 900:

        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+18444860059',
        to='+17726264537'
    )
    print(message.status)