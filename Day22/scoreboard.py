from turtle import Turtle

POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal") 


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()  # Only call this once
        
    def update_scoreboard(self):
        self.clear()  # Clear previous text first
        self.write(f"Player 1: {self.score_l} | Player2: {self.score_r}", align=ALIGNMENT, font=FONT)
    
    def increase_score_l(self):
        self.score_l += 1
        self.update_scoreboard()  # This will clear and rewrite

    def increase_score_r(self):
        self.score_r += 1 
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
