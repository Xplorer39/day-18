import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("red")


# DRAWS DASHED LINE
# for _ in range(50):
#     tim.forward(5)
#     tim.pu()
#     tim.forward(5)
#     tim.pd()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# DRAWS TRIANGLE-DECAGON
# def draw_shape1(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# def draw_shape2(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range (3,11):
#     tim.color(random.choice(colours))
#     draw_shape1(shape_side_n)
#     draw_shape2(shape_side_n)

# DRAWS RANDOM WALK
# directions = ["90", "180", "270", "0"]
# tim.pensize(15)
tim.speed("fastest")
#
# MAKES A RANDOM COLOR
def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color = (r, g, b)
    return color
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# DRAWS SPIROGRAPH
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)

screen.exitonclick()
