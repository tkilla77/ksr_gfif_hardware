from gturtle import *
from datetime import datetime

"""
optimized version: only draws something is changes
"""

L = 30

x_offset = -220
x_dist = 3*L
y_offset = 150

dark_mode = True

Options.setPlaygroundSize(600,600)

turi = Turtle()
turi.hideTurtle()

myblue = "blue"
if dark_mode:
    turi.clear(makeColor("black",0.9))
    myblue = "DodgerBlue"

def decimal_to_binary(z):
    binary = ""
    while(z >= 1):
        binary = str(z%2) + binary
        z = z//2
    while len(binary) < 6:
        binary = "0"+binary
    return binary

def draw_circle(x,y,col,width):
    turi.setPenColor(col)
    turi.setPenWidth(width)
    turi.setPos(x,y+L)
    turi.setHeading(0)
    turi.left(90)
    turi.leftArc(L,360)

def draw_cross(x,y,col,width):
    turi.setPenColor(col)
    turi.setPenWidth(width)
    turi.setPos(x-L,y-L)
    turi.setHeading(0)
    turi.right(45)
    turi.forward(L*2*1.41)
    turi.setPos(x+L,y-L)
    turi.setHeading(0)
    turi.right(-45)
    turi.forward(L*2*1.41)

def draw_square(x,y,col,width):
    turi.setPenColor(col)
    turi.setPenWidth(width)
    turi.setPos(x-L,y-L)
    turi.setHeading(0)
    repeat 4:
        turi.forward(2*L)
        turi.right(90)

def replace_char_at_index(s,c,i):
    # replace char at index i in string with char c
    return s[:i] + c + s[i+1:]

def show_clock(time):
    now = datetime.strptime("18/09/19 {0}".format(time), '%d/%m/%y %H:%M:%S')
    h = now.hour
    m = now.minute
    s = now.second
    h_bin = decimal_to_binary(h)
    m_bin = decimal_to_binary(m)
    s_bin = decimal_to_binary(s)

    for i in range(6):
        draw_circle(x_offset+i*x_dist,y_offset,"white",5)
        if h_bin[i] == "1":
            draw_circle(x_offset+i*x_dist,y_offset,"red",5)
        else:
            draw_circle(x_offset+i*x_dist,y_offset,"gray",2)            

        draw_cross(x_offset+i*x_dist,0,"white",5)
        if m_bin[i] == "1":
            draw_cross(x_offset+i*x_dist,0,myblue,5)
        else:
            draw_cross(x_offset+i*x_dist,0,"gray",2)
    
        draw_square(x_offset+i*x_dist,-y_offset,"white",5)
        if s_bin[i] == "1":
            draw_square(x_offset+i*x_dist,-y_offset,"green",5)
        else:
            draw_square(x_offset+i*x_dist,-y_offset,"gray",2)

    print(time)

show_clock("12:22:43")
#show_clock("00:00:00")








