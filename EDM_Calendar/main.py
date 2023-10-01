# # https://edmtrain.com/api-documentation
#
# import datetime
# import json
# import pytz
# import requests
# import pandas
#
# my_time_zone = pytz.timezone("America/Los_Angeles")
# now = datetime.datetime.now(my_time_zone).date()
# print(now)
# parameters = {
#     "client": "0d124bbc-6928-4b66-9e4a-501cf7f521ce",
#     "startDate": now,
#
# }
#
# response = requests.get(url="https://edmtrain.com/api/events?latitude=37.7749&longitude=-122.4194&state=California",
#                         params=parameters)
#
# data = response.json()["data"][:240]
#
# # for x in data_slice:
# #     artist = data_slice[0]["artistList"]
# #     print(artist[0])
# #
# # # for x in data
# # #     more_edm =
# #
# # print(data)
# events = pandas.DataFrame(data)
# new = events.iterrows()
# with open("test.json", mode="w") as file:
#     json.dump(data, file, indent=4)
#
# # for x in data:
# #     artist_list = x["artistList"]
# #     name_of_event=(x["name"])
# #     print(name_of_event)
# #     start_time= x["startTime"]
# #     end_time= x["endTime"]
# #     location = x["venue"]["location"]
# #     location_address = x["venue"]["address"]
# #     link = x["link"]
# #
# #     for i in artist_list:
# #         if "name" in i:
# #             print(i["name"])
# #     print(location)
#
#
# # for x in new:
# #     event_name = x[1]["name"]
# #     location_name = x[1]["venue"]["name"]
# #     list = {event_name,location_name}
# #
# #
# # print(list)
#
# # print(events.to_csv())
# # print(events)
# is_true= True
# while is_true:
#
#     for x in new:
#         artist_list = [i["name"] for i in x[1]["artistList"]]
#         # name_of_event =[i for i in x[1]["name"] if i is not None]
#         dict = {
#             "artist_list": ','.join(artist_list),
#             "Location": x[1]["venue"]["name"],
#             "name_of_event": x[1]["name"],
#
#         }
#
#         edm_frame = pandas.DataFrame(dict.values()).T
#         edm_frame_header = ','.join(dict.keys()).split(",")
#         print(edm_frame)
#         edm_frame.to_csv("EDM_Data.csv", mode="a",index=False)
#     # with open("EDM_Data.csv",mode="w") as file:
#     #     file.write(edm_frame)
import pip

pip install emmet
