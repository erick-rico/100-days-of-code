# with open("weather_data.csv") as data_file:
#     data_file = data_file.readlines()
#     print(data_file)
import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")

# --------------------------------------------------

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
# avg_temp1 = total_temp / len(temp_list)
# print(avg_temp1)

# avg_temp2 = sum(temp_list) / len(temp_list)
# print(avg_temp2)

# avg_temp3 = data["temp"].sum() / len(temp_list)
# print(avg_temp3)

# print(data["temp"].mean())
# print(data["temp"].max())

# --------------------------------------------------

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])
# print(data.iloc[0].to_numpy())
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# --------------------------------------------------

# Create a df from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data1 = pandas.DataFrame(data_dict)
data1.to_csv("new_data.csv")









