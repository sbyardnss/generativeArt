import uuid
from turtle import *

def create_file():
    file_name = uuid.uuid1()
    getscreen().getcanvas().postscript(file=f'output/tiling/tiling{file_name}.eps')
