# import colorgram
import turtle as t 
import random


def main():
    # rgb_colors = []
    print("Welcome to the Colorgram + Turtle.py project!")
    color_list = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]
    t.colormode(255)
    tim = t.Turtle()
    tim.penup()
    tim.speed("fastest")
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1 ):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)
        
    # colors = colorgram.extract('images.jpg', 30)
    # first_color = colors[0]
    # rgb = first_color.rgb 
    # hsl = first_color.hsl 
    # proportion = first_color.proportion 
    # print(f"RGB: {rgb.r}, HSL: {hsl} proportion: {proportion}")
    # for color in colors:
    #     r = color.rgb.r 
    #     g = color.rgb.g
    #     b = color.rgb.b 
    #     new_color = (r,g,b)
    #     rgb_colors.append(new_color)
    screen = t.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()