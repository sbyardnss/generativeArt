import uuid
from turtle import *

def create_file(name):
    file_name = uuid.uuid1()
    getscreen().getcanvas().postscript(file=f'output/{name}/{name}{file_name}.eps')
