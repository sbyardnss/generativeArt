from turtle import *
import random
from create_file import create_file
from theme import set_theme

set_theme()
fc = ["#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9', "#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9']

def draw_circle(size):
    circle(-size*.5)
def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
def draw_triangle(size):
    angle = random.randint(0,size)
    # right(angle)
    for i in range(3):
        forward(size)
        right(120)
    # left(angle)

def make_shapes(size):
    penup()
    # goto(-100, 100)
    for y in range(-size*9+size, (size*10)-1, size):
        for x in range(-size*9-size, (size*10)-1, size):
            # goto(x,y)
            num = random.randint(0, 3)
            begin_fill()
            if num == 0:
                goto(x+size*.5*.5+.5*size,y)
                draw_circle(size)
            elif num ==1:
                goto(x+size*.5*.5,y)
                draw_square(size)
            else:
                goto(x+size*.5*.5,y-.1*size)
                draw_triangle(size)
            fillcolor(fc[num])
            end_fill()
make_shapes(40)


tracer(True)
exitonclick()