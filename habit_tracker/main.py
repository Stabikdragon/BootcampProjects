import requests
import datetime

# to view graph https://pixe.la/v1/users/stabikdragon/graphs/codetime.html

PIXELA_ENDPOINT_URL = "https://pixe.la/v1/users"
USERNAME = "stabikdragon"
PASSWORD = "ptiimy2357"
GRAPH_ID = "codetime"
pixel_params={
    "token":PASSWORD,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# Already created User(4/6/23). response variable not necessary anymore
# response = requests.post(url=PIXELA_ENDPOINT_URL, json=pixel_params)
# print(response.text)

GRAPH_END_POINT_URL = f"{PIXELA_ENDPOINT_URL}/{USERNAME}/graphs"
graph_params={
    "id": GRAPH_ID,
    "name": "Coding Time!",
    "unit": "minutes",
    "type": "int",
    "color": "kuro"

}
headers = {
    "X-USER-TOKEN": PASSWORD
}
# response = requests.post(url=GRAPH_END_POINT_URL, json=graph_params, headers=headers)
# print(response.text)

POST_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/stabikdragon/graphs/{GRAPH_ID}"
today = datetime.datetime.now().strftime("%Y%m%d")

post_pixel_params={
    "date": today,
    "quantity": "10"
}
# response = requests.post(url=POST_PIXEL_ENDPOINT, headers=headers, json=post_pixel_params)
# print(response.text)
# print(today.strftime("%Y%m%d"))
UPDATE_PIXEL_ENDPOINT=f"https://pixe.la/v1/users/stabikdragon/graphs/{GRAPH_ID}/{today}"
update_params={
    "quantity":"20"
}

response = requests.delete(url=UPDATE_PIXEL_ENDPOINT,headers=headers)

print(response)