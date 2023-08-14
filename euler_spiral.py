from turtle import *
from create_file import create_file
from theme import set_theme
import random


def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

# penup()
# goto(0, 200)
# pendown()
set_theme(canvas_height=1000,
          canvas_width=1000,
          tracer_value=0,
          hide_turtle=True)
# # euler_curve(step_size=40, angle_step=1.00, n_steps=600)
# euler_curve(step_size=7, angle_step=.66, n_steps=10000)
# set_theme(tracer_value=0)
# euler_curve(step_size=2, angle_step=1.01, n_steps=100000)
# set_theme(tracer_value=0)
euler_curve(step_size=3, angle_step=1.99, n_steps=100000)
tracer(True)
exitonclick()
