# import colorgram

# colors = colorgram.extract('./image.jpg', 10)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb_colors.append((r,g,b))

# print(rgb_colors)

from turtle import Turtle , Screen
import turtle as t
import random
color_list = [(254, 254, 253), (249, 254, 252), (254, 249, 252), (237, 247, 252), (226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215)]

tim = Turtle()
t.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fastest")


start_x = -250
start_y = -250
for row in range(10):
    for col in range(10):
        tim.goto(start_x + col * 50, start_y + row * 50)
        tim.dot(20, random.choice(color_list))
    
screen = Screen()
screen.exitonclick()

