# How to Use OOP
# Attributes (Variables) and Methods (Function)

# Constructing Objects
# car = CarBluePrint() 
# Object =  Class

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)  #object.attribute

# # Object Methods ---> object.method()
# my_screen.exitonclick()

# Python Packages (pypi.org)
# pip install package
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric" , "Water", "Fire"])

table.align = "l"

print(table)



