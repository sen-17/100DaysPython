from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220 , 260)
        self.level = 1
        self.current_level() 
    
    def current_level(self):
        self.write(f"Level: {self.level}", align = "center", font = FONT)

    def increase_level(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center" , font = FONT)
