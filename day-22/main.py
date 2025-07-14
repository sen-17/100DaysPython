from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350 , 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down , "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down , "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()
       
    if ball.xcor() < -400:
        score.r_point()
        ball.reset_position()



screen.exitonclick()

