from turtle import Turtle

POSITION = (-200, 250)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal") 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.penup()
        self.color("black")
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()  # Only call this once
    
    def update_scoreboard(self):
        self.clear()  # Clear previous text first
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.level += 1 
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
