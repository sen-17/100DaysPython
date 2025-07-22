# Catching Exceptions
# File Not Found
# KeyError
# Index Error
# Type Error

# try:
# except:
# else:
# finally:

try:
    with open("a_file.txt", mode="r") as file:
        file.write("Hello")
except FileNotFoundError:
    print(f"File not detected")

# Raising Exceptions
# raise KeyError
# raise TypeError , etc , etc

# JSON
# json.dump() - write
# json.load() - read
# json.update() - update


