from turtle import *
from theme import set_theme
import random

set_theme(canvas_width=1200,
          canvas_height=800,
          thickness=1,
          )

# size of letters
size = 50
# number of connecting points
n = 1
for y in range(400 - size, -400, -size):
    # change color for every row
    r = random.random()
    g = random.random()
    b = random.random()
    pencolor(r,g,b)
    prime = random.random()

    for x in range(-600+size, 600, size):
        # change color for every letter
        # r = random.random() * prime
        # g = random.random() * prime
        # b = random.random() * prime
        # pencolor(r, g, b)
        # original point within letter
        px = x + random.uniform(-size/4, size/4)
        py = y + random.uniform(-size/4, size/4)

        # start point on canvas. set to original point
        px_start = px
        py_start = py

        # move to starting point
        penup()
        goto(px_start, py_start)
        pendown()

        # draw the shape
        for i in range(n):
            # random end point
            px_end = x + random.uniform(-size/4, size/4)
            py_end = y + random.uniform(-size/4, size/4)

            # draw connecting ling
            goto(px_end, py_end)

            # reset starting point
            px_start = px_end
            py_start = py_end

        # go back to original point
        goto(px, py)
    # increase n
    n += 3


tracer(True)
exitonclick()
