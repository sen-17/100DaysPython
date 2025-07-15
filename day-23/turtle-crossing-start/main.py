import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun = player.move_forward , key = "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.current_level()

    if -300 < player.ycor() < 290:
        car.create_car()
        car.move_cars()

    if player.ycor() > 280:
        car.increase_speed()
        player.reset_position()
        score.increase_level()

    for car_obj in car.all_cars:
        if player.distance(car_obj) < 20:
            game_is_on = False
            score.game_over()
            player.reset_position()
    
screen.exitonclick()

