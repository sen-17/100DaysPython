from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40 , 0)]
MOVE_STEP = 20
class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
        
    def create_snake(self):   
        for position in STARTING_POSITION:
            self.add_segments(position)
            
    def add_segments(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position) 
        self.all_segments.append(snake)
        
    def extend(self):
        self.add_segments(self.all_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1 , 0 , -1):
            new_x = self.all_segments[seg_num - 1 ].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x , new_y)
        
        self.head.forward(MOVE_STEP)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
       
        