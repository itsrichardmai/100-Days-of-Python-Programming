from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(90)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)
            
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y :
            return True 
        else: 
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
