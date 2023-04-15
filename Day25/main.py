# with open("./weather-data.csv") as weather_data:
#     weather = weather_data.readlines()
# print(weather)

# import csv
#
# with open("./weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather-data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# print(temp_list)
#
# # average = sum(temp_list)/len(temp_list)
# # print(round(average, 2))
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# celcius_temp = monday.temp
# print(celcius_temp*1.8 + 32)

squirrels = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# color = squirrels["Primary Fur Color"]
# gray_squirrels = squirrels[color == "Gray"]["Primary Fur Color"].count()
# cinnamon_squirrels = squirrels[color == "Cinnamon"]["Primary Fur Color"].count()
# black_squirrels = squirrels[color == "Black"]["Primary Fur Color"].count()

gray_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

squirrels_data = [{
    "fur color": "Gray",
    "count": gray_squirrels
},
{
    "fur color": "Black",
    "count": black_squirrels
},
{
    "fur color": "Cinnamon",
    "count": cinnamon_squirrels
},
]

squirrels_dataframe = pandas.DataFrame(squirrels_data)
squirrels_dataframe.to_csv("squirrels.csv")
print(squirrels_dataframe)