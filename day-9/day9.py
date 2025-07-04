# Dictionaries and Nesting

# {Key : Value}

colours = {
    "apple" : "red",
    "pear" : "green",
    "banana" : "yellow"   
}

# Retrieve Items
print(colours["pear"]) # Green 

# Add New Items
colours["peach"] = "pink"

# Edit existing items
colours["apple"] = "purple"

print(colours)

# Wipe an existing dictionary
# colours = {}

# Loop through a dictionary
for key in colours:
    print(key)
    print(colours[key])

# {Key1 : [list]
#  Key2 : {Dict}
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"]
# }

# print(travel_log["France"][1]) # Lille

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1]) # D

travel_log = {
    "France": {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])

# Max function in dictionaries
fruits = {"apple" : 2, "pear" : 4, "orange" : 9}
max(fruits, key=fruits.get)


