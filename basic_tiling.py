import random
import tkinter as tk
from turtle import *
from svg_turtle import SvgTurtle
from theme import set_theme
from create_file import create_file

width = 1000
height = 1000
setup(width, height)
# speed('fastest')

# tracer(False)


def tiling(x, y, s, l, mode="straight"):
    # we have reached the final level of recursion
    # and we now draw
    if l == 0:
        if mode == "straight":
            if random.random() < 0.5:
                # vertical line
                penup()
                goto(x, y-s)
                pendown()
                goto(x, y+s)
            else:
                # horizontal line
                penup()
                goto(x-s, y)
                pendown()
                goto(x+s, y)
        elif mode == 'diagonal':
            if random.random() < 0.5:
                # top left to bottom right
                penup()
                goto(x-s, y+s)
                pendown()
                goto(x+s, y-s)
            else:
                # bottom left top right
                penup()
                goto(x-s, y-s)
                pendown()
                goto(x+s, y+s)
    # split screen and go to next level of recursion
    else:
        s /= 2
        l -= 1
        tiling(x-s, y+s, s, l, mode)
        tiling(x+s, y+s, s, l, mode)
        tiling(x-s, y-s, s, l, mode)
        tiling(x+s, y-s, s, l, mode)

# width(2)


hideturtle()
tracer(False)
# speed('fastest')
# dont go past 7 levels
tiling(0, 0, 400, 5, 'diagonal')
tracer(True)
# create_file('tiling')
exitonclick()
