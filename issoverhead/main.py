import requests
from datetime import datetime
import math
import time

MY_LAT = -40.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude



response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data1 = response1.json()

iss_latitude = float(data1["iss_position"]["latitude"])
iss_longitude = float(data1["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

split_lat = math.trunc(MY_LAT)
split_long = math.trunc(MY_LONG)

lat_range = list(range(split_lat-5, split_lat+5))
long_range = list(range(split_long-5, split_long+5))
current_location= (lat_range,long_range)
sunnny = list(range(sunrise, sunset))

if math.trunc(iss_latitude) in current_location[0] or math.trunc(iss_longitude in current_location[1]):
    if time_now.hour not in sunny:
        print("yes")


