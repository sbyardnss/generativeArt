from turtle import *
import random
import math
from theme import set_theme


set_theme(hide_turtle=False, speed_value='fastest', tracer_value=1)


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
    # goto start location
    s_point = pt(-200, 0)
    goto(-200, 0)
    pendown()
    # find initial point of turtle (tr_init) and angle to vanishing point
    angle_start = findAngle(s_point, vp)
    left(angle_start)

    # draw left of box upward

    forward(y_init)
    top_left_pt = position()

    # if new x_length not defined, draw top of box with x_init and 
    # define to new variable (only one iteration with x_init)
    new_angle = angle_start - 360
    right(new_angle)
    forward(x_init)
    top_right_pt = position()
    # print(top_right_pt)
    distance_between_tl_tr = distance(top_left_pt, top_right_pt)
    
    # turn right and draw right side
    print(top_right_pt[0])
    new_angle = findAngle(pt(vp.x, vp.y),pt(top_right_pt[0], top_right_pt[1]))
    right(-new_angle)
    print(s_point.x)
    while position()[1] > s_point.y:
        forward(10)

    # turn right and draw bottom
    goto(s_point.x, s_point.y)

    



# 225.0

draw_lines(xi, yi)
tracer(True)
exitonclick()
