from turtle import *
import random
from theme import set_theme
from create_file import create_file
import tkinter as tk
set_theme(canvas_color="black")

# write("HF", move=True, align="center", font=("futura", 200, 'normal'))
# write("Hf", align="center", font=("arial", 200, 'normal'))
t = "STEPHEN"
fc = ["#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9', "#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9']

def write_letters(text):
    penup()
    goto(0, -200)
    f_size = 500
    # iterate text
    current_x = 0
    # current_y = -300
    reverse = text[::-1]
    for i in range(len(text)):
        current_x = f_size*.5
        current_y = f_size*.5
        # if i %2 == 0:
        #     color('whitesmoke')
        # else:
        color(fc[i])
        write(text[i], move=False, align="right", font=("futura", int(f_size), 'bold'))
        f_size *= .7
        goto(-current_x+200,  -current_y)
        # current_x += 60
        # current_y += 30
    # add letter at current font size
    # make font size .8 size
    # add next letter
    # 
write_letters(t)
# write((0,0), True)
tracer(True)
exitonclick()