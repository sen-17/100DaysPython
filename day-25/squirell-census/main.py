import pandas

data = pandas.read_csv(r"100DaysPython\day-25\squirell-census\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250715.csv")
fur_color = data["Primary Fur Color"].to_list()

gray_fur = 0
cinnamon_fur = 0
black_fur = 0

for fur in fur_color:
    if fur == "Gray":
        gray_fur += 1
    elif fur == "Cinnamon":
        cinnamon_fur += 1
    elif fur == "Black":
        black_fur += 1

data_dicts = {
    "Fur Color": ["Gray" , "Cinnamon", "Black"],
    "Count" : [gray_fur , cinnamon_fur , black_fur]
}

convert_table = pandas.DataFrame(data_dicts)
convert_table.to_csv(r"100DaysPython\day-25\squirell-census\new_data.csv")

