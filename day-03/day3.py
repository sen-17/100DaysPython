# Conditionals Statement
# If else statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster")
else:
    print("You can't ride the roller coaster")

# Modulo Operator (%)
print (10 % 2) # Output : 0
print (10 % 3) # Output : 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if statements and elif
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
    
else:
    print("You can't ride the roller coaster")