from turtle import Turtle, Screen
import random

def main():

    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    try:
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        if user_bet not in colors:
            raise ValueError("Choose a color 'red', 'blue', 'green', 'orange', 'yellow', 'purple")
    except ValueError as e:
        print(f"Error: {e}")

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        new_turtle.color(colors[turtle_index])
        all_turtles.append(new_turtle)
    print(all_turtles)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle   is the winner!")
            random_distance = random.randint(0, 10)    
            turtle.forward(random_distance)



    screen.exitonclick()

if __name__ == '__main__':
    main()
