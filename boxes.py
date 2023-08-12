from turtle import *
from theme import set_theme
import random
import math

set_theme(canvas_width=1800, thickness=2)

size = 30
# noise = 0.0
for y in range(400, -400, -size):
    for x in range(-700, 700, size):
        # move to location
        penup()
        goto(x,y)
        pendown()

        # rotate square
        max_distance = math.sqrt(800**2 + 400**2)
        distance = math.sqrt(x**2 + (7/4)**2 * y**2 /.8)
        noise = (max_distance - distance)/15
        noise = noise if noise > 15 else 0
        angle = random.uniform(-noise, noise)
        right(angle)

        # draw
        for i in range(4):
            forward(size)
            right(90)
        # rotate back so that later squares not affected by earlier squares
        left(angle)
    # add noise
    # noise+= 2

tracer(True)
exitonclick()