# # with open("weather_data.csv") as file:
# #     list = file.readlines()
# #     print(list)
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data  = csv.reader(file)
# #     temps = []
# #     for i in data:
# #         if i[1] != "temp":
# #             temps.append(int(i[1]))
# #     print(temps)
# import statistics
import pandas
# data = pandas.read_csv("weather_data.csv")
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# length = len(temp_list)
# total = 0
#
# for i in temp_list:
#     total += i
# # print(total/length)
#
# row = data["temp"].max()
#
# # print(data[data["temp"] == row ])
#
# monday = data[data.day == "Monday"]
# # print(monday.temp.rmul(1.8)+32)
# # with open("./weather)
#
# data_dict = {
#     "student": ["amy", "james", "angela"],
#     "scores": [76, 56, 65 ]
# }
#
# data = pandas.DataFrame(data_dict)
#
# # print(data)
#
# data.to_csv("./data.txt")



#TODO: create csv called squirrel count that has a small table, that contains fur color and how many squirrels


data2 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = "Primary Fur Color"

gray = len(data2[data2[fur_color] == "Gray"])
red = len(data2[data2[fur_color] == "Cinnamon"])
black = len(data2[data2[fur_color] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cin", "Black"],
    "Count": [gray, red, black]

}
frame = pandas.DataFrame(data_dict)

frame.to_csv("./test.txt")
