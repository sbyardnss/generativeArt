from turtle import *
import random
from create_file import create_file
from theme import set_theme

set_theme(canvas_color='gray')
fc = ["#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9', "#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9']

def draw_circle(size):
    circle(-size*.5)
def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
def draw_triangle(size, angle_bool):
    angle = random.randint(0,size)
    if angle_bool == True:
        right(angle)
    for i in range(3):
        forward(size)
        right(120)
    if angle_bool == True:
        left(angle)

def make_shapes(size):
    penup()
    # goto(-100, 100)
    for y in range(400, -400, -size):
        for x in range(-400, 400, size):
            num = random.randint(0, 2)
            begin_fill()
            if num == 0:
                goto(x+size*.5,y)
                draw_circle(size)
            elif num ==1:
                goto(x,y)
                draw_square(size)
            # elif num ==3:
            #     None
            else:
                goto(x,y-.1*size)
                if y < 100:
                    draw_triangle(size, True)
                else:
                    draw_triangle(size, False)
            # fillcolor(fc[num])
            if num ==2:
                if y < -100:
                    fillcolor(fc[0])
                elif y < 0:
                    fillcolor(fc[1])
                elif y < 100:
                    fillcolor(fc[2])
                elif y< 200:
                    fillcolor(fc[3])
                elif y< 300:
                    fillcolor(fc[4])
                else:
                    fillcolor(fc[5])
                # fillcolor('maroon')
            elif num ==1:
                fillcolor('teal')
            else:
                print(num)
                fillcolor('black')
            end_fill()
make_shapes(40)


tracer(True)
# create_file('shapes')
exitonclick()