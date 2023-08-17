from turtle import *
import random
import math
from theme import set_theme
from create_file import create_file

# set_theme(hide_turtle=False, speed_value='fast', tracer_value=1)
set_theme()

# def draw_lines():
#     speed(0)
#     penup()
#     goto(-200, 200)
#     pendown()
#     distance = 400
#     vertical_spacing = 20
#     for i in range(10):
#         forward(distance)
#         penup()
#         backward(distance+50)
#         right(90)
#         forward(vertical_spacing)
#         left(90)
#         pendown()
#         distance += 120
#         vertical_spacing += 10

# def draw_lines():
#     # first line will be 100 wide
#     # starting at -50
#     # length of full line for loop
#     x_half_length = 50

#     # increment of width increase for each square?
#     x_size = 10

#     # length of space between lines. starting at 10
#     y_length = 10

#     # vertical positioning of lines starting at 400
#     y_position = 300
#     penup()
#     goto(-50, y_position)
#     for i in range(10):
#         for x in range(-x_half_length, x_half_length, x_size):
#             # create ten cells
#             goto(x, y_position)
#             pendown()
#             goto(x+x_size, y_position)
#             goto(x-x_size, y_position-y_length)
#             goto(-x, y_position-y_length)
#             penup()
#         # increase y_position, y_length, x_length, x_half_length
#         y_position -= y_length
#         y_length += 10
#         x_size += 10
#         # x_half_length += x_half_length/10

class pt():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point(self):
        return (self.x, self.y)
ptA = pt(10, 10)
ptB = pt(0, 1000)
def findAngle(pt1, pt2):
    import math
    dy = pt2.y - pt1.y
    dx = pt2.x - pt1.x
    if dx == 0:
        return 180.0
    else:
        return math.atan2(dy, dx) * 180.0 / math.pi
# print(findAngle(ptA, ptB))

# define vanishing point
v_point = pt(0, 1000)
s = pt(-200, 0)
# print(findAngle(v_point, s))
xi = 50
yi = 40
def draw_lines(x_init, y_init):
    vp = pt(0, 1000)
    penup()

    # define point for beginning of row
    s_point = pt(0, 100)
    
    # define first vertical distance
    goto(0, 100)
    pendown()

    # changeable start point for each cell
    start_for_cell = s_point
    
    # other starting corners
    next_distance = y_init
    for i in range(60):
        fc = ["#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9', "#fa6edb", "#d882f5", '#af94ff', '#80a2ff', '#4aadff', '#00b5ff', '#00baf0', '#00bddd', '#35bfca', '#5bbfb9']
        for i in range(10):
            begin_fill()
            pendown()
            # find initial point of turtle (tr_init) and angle to vanishing point
            angle_start = findAngle(pt(position()[0], position()[1]), vp)
            left(angle_start)

            # draw left of box upward

            # travelling up left side
            forward(next_distance)
            top_left_pt = position()

            # if new x_length not defined, draw top of box with x_init and 
            # define to new variable (only one iteration with x_init)
            new_angle = angle_start - 360
            right(new_angle)

            # travelling right across top
            forward(x_init)
            top_right_pt = position()
            # print(top_right_pt)
            distance_between_tl_tr = distance(top_left_pt, top_right_pt)
            
            # turn right and draw right side
            new_angle = findAngle(pt(vp.x, vp.y),pt(top_right_pt[0], top_right_pt[1]))
            right(-new_angle)
            # travelling down right side
            end_fill()
            fillcolor(fc[i])
            while position()[1] > start_for_cell.y and distance(top_right_pt, (position()[0], position()[1])) < 300:
                forward(10)
            next_cell_start = pt(xcor(), ycor())
            next_distance = distance(top_right_pt, (next_cell_start.x, next_cell_start.y))
            # turn right and draw bottom
            goto(start_for_cell.x, start_for_cell.y)
            start_for_cell = next_cell_start
            penup()
            goto(start_for_cell.x, start_for_cell.y)
            right(new_angle)
        next_distance = y_init * 1.2
        # go to next starting point
        penup()
        goto(s_point.x, s_point.y)
        left(356)
        forward(next_distance)

    



# 225.0

draw_lines(xi, yi)
tracer(True)
# create_file('wave')
exitonclick()
