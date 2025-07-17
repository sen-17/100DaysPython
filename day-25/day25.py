# Reading CSV 
# with open(r"100DaysPython\day-25\weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open(r"100DaysPython\day-25\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for rows in data:
#         if rows[1] != "temp":
#             temperatures.append(int(rows[1]))
    
#     print(temperatures)

# Python data analysis library - pandas
import pandas

data = pandas.read_csv(r"100DaysPython\day-25\weather_data.csv")
print(data["temp"]) # Get data

# Data Frames and Series
print(type(data)) # Data Frames = Whole table
print(type(data["temp"])) # Series , kinda like a List

data_dict = data.to_dict() # Converting data into a dictionary
print(data_dict) 

temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list) 
# print(average)

print(data["temp"].mean()) # average
print(data["temp"].max()) # max value

print(data.condition) # different approach than []

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dicts = {
    "students" : ["Amy", "James", "Angela"],
    "Scores": [76,56,65]
}
convert_to_table = pandas.DataFrame(data_dicts)
convert_to_table.to_csv("new_data.csv")