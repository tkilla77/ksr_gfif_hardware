from gturtle import *
Options.setPlaygroundSize(800,600) 

fritz = Turtle()
fritz.hideTurtle()

"""
repeat 4:
    fritz.leftArc(100,180)
    fritz.left(90)
"""

fritz.setPos(0,0)
repeat 2:
    fritz.leftArc(100,360)
    fritz.left(180)
fritz.setPos(-200,0)
fritz.left(180)
fritz.leftArc(200,360)
fritz.setPos(-100,0)
fritz.dot(40)
fritz.setPos(100,0)
fritz.dot(40)

