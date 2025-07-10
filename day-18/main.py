from turtle import Turtle, Screen 
import turtle as t
import random

# Python Tuples (immutable)
my_tuples = (1,2,3)

my_tuples[1] # accessing tuples


tim = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)

    random_color =  (r , g , b)
    return random_color


# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range (num_side):
#         tim.forward(100)
#         tim.right(angle)

# for n_side in range(3,11):
#     draw_shape(n_side)


direction = [
    0,90,180,270
]

def random_walk():
    tim.pensize(15)
    tim.speed(5)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

for _ in range(100):
    random_walk()


screen = Screen()
screen.exitonclick()
