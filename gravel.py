from turtle import *
from theme import set_theme
import random

set_theme(canvas_width=600, thickness=2)

size = 50
noise = 0.0
fc = ["#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9', "#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9']

for y in range(400, -400, -size):
    for x in range(-250, 250, size):

        # move to location
        penup()
        goto(x,y)
        
        pendown()
        # begin_fill()
        # rotate square
        angle = random.uniform(-noise, noise)
        right(angle)

        # draw
        for i in range(4):
            forward(size)
            right(90)
        # if noise > 4:
        #     fillcolor(fc[int(noise/2)])
        # else:
        #     fillcolor(fc[0])
        # end_fill()
        # rotate back so that later squares not affected by earlier squares
        left(angle)
    # add noise
    noise+= 1


tracer(True)
exitonclick()
