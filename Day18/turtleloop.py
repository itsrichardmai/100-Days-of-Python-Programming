from turtle import Turtle, Screen
import random
# import heroes 

# set screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.title('Object-Oriented Turtle Demo')
screen.bgcolor("sky blue")

# define turtle 
tim = Turtle()

tim.color("green")
tim.shape("turtle")
tim.fillcolor("black")

directions = [0, 90, 180, 270]
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue']
# draw shapes triangle - decagon using function to change degree of angles. 
# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)



for _ in range(200):
    tim.color(random.choice(colors))
    tim.pensize(random.randint(1, 100))
    tim.forward(30)
    tim.speed("fastest")
    tim.setheading(random.choice(directions))

# Draw a triangle 
# Draw a square
# Draw a pentagon
# Draw a hexagon
# heptagon
# octagon
# nonagon
# decagon 

screen.exitonclick()
