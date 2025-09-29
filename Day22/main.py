from turtle import Screen, Turtle
from paddle import Paddle 
from ball import Ball 
import time 
from scoreboard import Scoreboard 

def main():
    

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Key event listener
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")


    game_is_on = True
    while game_is_on:
        time.sleep(0.05)
        screen.update()
        ball.move()
        # Detect collision with the wall - ball hit wall 
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce_y()
        # Detect collision with right paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        # Detect when right paddle misses 
        if ball.xcor() > 380:
            scoreboard.increase_score_l()
            ball.reset_position()
        # Detect when left paddle misses 
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_score_r()
        
    screen.exitonclick()


if __name__ == '__main__':
    main()
