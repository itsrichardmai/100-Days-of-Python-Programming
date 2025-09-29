import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():

    screen = Screen()
    player = Player() 
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.setup(width=600, height=600)
    screen.tracer(0)
    # Listen for player event 
    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_cars()
        car_manager.move_cars()
        # Detect collision with car 
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
            # Detect if player is at finish line of ycor 280+ 
            if player.is_at_finish_line():
                scoreboard.increase_score()
                player.go_to_start()
        
    screen.exitonclick()

if __name__ == '__main__':
    main()