from turtle import *
import random
import math
from theme import set_theme


set_theme(hide_turtle=False, speed_value='fastest', tracer_value=1)


# def draw_lines():
#     speed(0)
#     penup()
#     goto(-200, 200)
#     pendown()
#     distance = 400
#     vertical_spacing = 20
#     for i in range(10):
#         forward(distance)
#         penup()
#         backward(distance+50)
#         right(90)
#         forward(vertical_spacing)
#         left(90)
#         pendown()
#         distance += 120
#         vertical_spacing += 10

def draw_lines():
    # first line will be 100 wide
    # starting at -50
    # length of full line for loop
    x_half_length = 50

    # increment of width increase for each square?
    x_size = 10

    # length of space between lines. starting at 10
    y_length = 10

    # vertical positioning of lines starting at 400
    y_position = 300
    penup()
    goto(-50, y_position)
    for i in range(10):
        for x in range(-x_half_length, x_half_length, x_size):
            # create ten cells
            goto(x, y_position)
            pendown()
            goto(x+x_size, y_position)
            goto(x-x_size, y_position-y_length)
            goto(-x, y_position-y_length)
            penup()
        # increase y_position, y_length, x_length, x_half_length
        y_position -= y_length
        y_length += 10
        x_size += 10
        # x_half_length += x_half_length/10
draw_lines()
tracer(True)
exitonclick()
