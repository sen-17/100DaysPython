from turtle import Turtle , Screen 
import turtle as t
import random


colours = ["red" , "orange", "yellow", "green", "blue", "purple"]
names = ["alex" , "tim", "bob", "tom", "steve" , "cream"]

screen = Screen()
screen.setup(width = 500 , height = 400)
user_guess = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Input a colour")


def create_turtle(name, x , y, colour):
    name = Turtle(shape = "turtle")
    name.penup()
    name.color(colour)
    name.goto(x,y)

    return name
    

x = -230
y = -90

random_colours = random.sample(colours, len(names))
all_turtles = []

for i in range(len(names)):
    turtles = create_turtle(names[i], x , y , random_colours[i])
    all_turtles.append(turtles)
    y += 30

race_on = True

while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            race_on = False

            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the winning color {winning_color} turtle won the race.")
            break
       
screen.exitonclick()




