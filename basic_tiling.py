import uuid
import random
import tkinter as tk
from turtle import *
from svg_turtle import SvgTurtle
from PIL import Image
# turtle.setup(1000, 1000)
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
file_name = uuid.uuid1()
getscreen().getcanvas().postscript(file=f'output/tiling/tiling{file_name}.eps')
# ps_image = Image.open('output/tiling80927ee0-388d-11ee-9a50-8c859040d697.ps')
# ps_image.save('output/tiling80927ee0-388d-11ee-9a50-8c859040d697.png')
exitonclick()
# def write_file(function, file, w, h):
#     t = SvgTurtle(w, h)
#     function(t)
#     t.save_as(file)

# write_file(tiling(0,0,400,5, 'diagonal'), f'{file_name}.svg', width, height)
