# Debugging
# 1. Describe the Problem
# 2. Reproduce the Bug
# 3. Play Computer (Pretend to be a Computer)
# 4. Fix the Errors (underline)

try:
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You are {age} years old")
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical number")

# 5. Print is Your Friend
# 6. Use a Debugger