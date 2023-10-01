import requests
import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#

MY_LAT = 37.368832

MY_LONG = -122.036346


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)