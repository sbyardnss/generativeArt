from turtle import *
from theme import set_theme
from create_file import create_file
import random


set_theme(canvas_height=1000,
          canvas_width=1000,
          canvas_color=(.23, .13, .46),
          pen_color='red')


def grow(length, decrease, angle, noise=0):
    if length > 10:
        width(length/10)
        forward(length)
        
        new_length = length * decrease
        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)
        angle_l = angle + random.gauss(0, noise)
        angle_r = angle + random.gauss(0, noise)

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        left(angle_r)
        backward(length)


penup()
goto(0, -300)
pendown()
left(90)
grow(150, .8, 30, 8)

tracer(True)
exitonclick()
