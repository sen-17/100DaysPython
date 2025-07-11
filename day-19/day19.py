# Higher Order Functions and Instances
from turtle import Screen , Turtle

# Instances
tim = Turtle()
tom = Turtle()

# State
tim.color("green")
tom.color("purple")

def move_forwards():
    tim.forward(10)

screen = Screen()
screen.setup(width = 500, height = 400)
screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race? Enter a colour")
screen.listen()
screen.onkey(key="space", fun = move_forwards) # Functions as Input
screen.exitonclick()