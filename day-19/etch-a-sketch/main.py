from turtle import Turtle , Screen
import turtle as t

tim = Turtle()
tim.speed(7)
def forward():
    tim.forward(20)

def backwards():
    tim.backward(20)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    t.resetscreen()
   
screen = Screen()
screen.listen()
screen.onkey(key="w" , fun = forward)
screen.onkey(key="s" , fun = backwards)
screen.onkey(key="a" , fun = left)
screen.onkey(key="d" , fun = right)
screen.onkey(key="c", fun = clear)
screen.exitonclick()