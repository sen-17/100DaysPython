from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_path = r"100DaysPython\day-20\data.txt"
        with open(self.file_path , mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
        
    def update_score(self): 
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align="center", font=('Courier', 20 ,'normal') )
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Courier', 20 ,'normal') )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.file_path = r"100DaysPython\day-20\data.txt"
            with open(self.file_path , mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()   


