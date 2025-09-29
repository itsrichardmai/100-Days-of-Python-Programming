from turtle import Screen, Turtle
from snake import Snake  
import time 
from food import Food 
from scoreboard import Scoreboard 

def main():


    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0) 
    
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    scoreboard.save_score()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1) 
        
        snake.move()
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()       
            scoreboard.save_score()
        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()
            print(f"You died! Your score was {scoreboard.score} Your highscore was {scoreboard.high_score}")

        # Detect collision with tail 
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                scoreboard.save_score()
    screen.exitonclick()


if __name__ == "__main__":
    main()

