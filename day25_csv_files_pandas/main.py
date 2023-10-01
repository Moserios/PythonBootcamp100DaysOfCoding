


# with open("source/weather_data.csv") as file:
#     data = file.readlines()
# print(data)
#
##############
# import csv
# with open("source/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     temp = []
#     for row in data:
#         temp.append(row[1])
#         print(row)
#     del temp[0]
#     for t in temp:
#         temperatures.append(int(t))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("source/weather_data.csv")
# # print(type(data))
# print(data["temp"])
# print(data)
#
# ### COLUMNS
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
# avg_temp = sum(temp_list) / len(temp_list)
#
# print(avg_temp)
# print(data["temp"].mean())
# print(data.temp.mean())
# print(data["temp"].max())
# print(data.temp.max())

### ROWS
#
# print(data[data.day == "Tuesday"])
#
# max_t = data.temp.max()
# print(max_t)
# print(data[data.temp == max_t])

# monday = data[data.day == "Monday"]
# # print(monday)
# print(monday.temp)
# monday_fahrenheit = monday.temp[0] * (9/5) + 32   #F = °C × (9/5) + 32
# print(monday_fahrenheit)

# create a dataframe from scratch

# data_dict = {
#     "students": ["Sergey", "Tatiana", "Andrey"],
#     "scores": [80, 95, 100]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#### central park squirrel challange ###

import pandas

data = pandas.read_csv("source/2018_Central_Park_Squirrel_Census_-_Squirrel_Data(1).csv")
# print(data["Highlight Fur Color"])
fur_colors = data["Primary Fur Color"].to_list()
print(fur_colors)
cinnamon_list = []
gray_list = []
black_list = []
for color in fur_colors:
    if color == "Cinnamon":
        cinnamon_list.append(color)
    if color == "Gray":
        gray_list.append(color)
    if color == "Black":
        black_list.append(color)

print(len(cinnamon_list))
print(len(gray_list))
print(len(black_list))

squirrel_count = {"Fur color": [],
                  "Count": []}

squirrel_count["Fur color"].append("cinnamon")
squirrel_count["Count"].append(len(cinnamon_list))
squirrel_count["Fur color"].append("gray")
squirrel_count["Count"].append(len(gray_list))
squirrel_count["Fur color"].append("black")
squirrel_count["Count"].append(len(black_list))


squirrels = pandas.DataFrame(squirrel_count)
squirrels.to_csv("squirrel_count.csv")

print(squirrel_count)
print(squirrels)


#### Bootcamp solution ####

red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

total_count = {"Fur color": ["Cinnamon", "Gray", "Black"],
                  "Count": [red_count, gray_count, black_count]}

df = pandas.DataFrame(total_count)
df.to_csv("titorial_version.csv")
