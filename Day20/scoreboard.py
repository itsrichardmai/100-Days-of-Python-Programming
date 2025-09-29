from turtle import Turtle

POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal") 


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode="r") as data:
            self.high_score = int(data.read())
        
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()  # Only call this once
        
    def update_scoreboard(self):
        self.clear()  # Clear previous text first
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # This will clear and rewrite

    # def game_over(self):
        # self.goto(0,0)
        # self.write("GAME OVER! YOUR SNAKE DIED", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score 
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 
        self.update_scoreboard()
    def save_score(self):

        with open('data.txt', mode="w") as file:
            file.write(f"\n{self.high_score}")
