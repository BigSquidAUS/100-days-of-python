# data = []
# with open("weather_data.csv") as weather_data:
#     for data_set in weather_data.readlines():
#         data_set = data_set.strip()
#         data.append(data_set)
#
# print(data)

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp": # Skip column heading "temp" in the .csv file.
#             temp = row[1]
#             temperatures.append(int(temp))
#
# print(temperatures)

import pandas
# https://pandas.pydata.org

data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# print(data["temp"])
# print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
# print(f"{average_temp:.2f}")

print(data["temp"].mean())
print(data["temp"].max())

# Get Data in columns
print(data.temp) # is the same as:
print(data["temp"])

# Get Data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) # Gets row where temp was maximum.

# Challenge 1
monday = data[data.day == "Monday"]

temp_C = monday.temp[0]
temp_F = (temp_C * 9/5) + 32

print(f"\nMonday: {temp_C}C | {temp_F}F")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy","James", "Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")