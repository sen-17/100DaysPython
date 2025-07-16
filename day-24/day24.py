
# Read file
# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write file
# with open("file.txt", mode="w") as file:
#     file.write("New text.")
#     contents = file.read()
#     print(contents)

# check file
# import os
# file_path = r"100DaysPython\day-24\file.txt"

# if os.path.exists(file_path):
#     print(True)
# else:
#     print(False)


# Appending
with open(r"100DaysPython\day-24\file.txt" , mode="a") as file:
    file.write("\nNew text.")
 
# Relative and Absolute File Path
# Absolute : Starts from the Root
# Relative : Starts from the working directory