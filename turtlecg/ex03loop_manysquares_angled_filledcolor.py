# -*- coding: utf-8 -*-
import turtle
from colors import randomcolor


def drawsquare(squareme):
    squareme.forward(40)
    squareme.left(90)
    squareme.forward(40)
    squareme.left(90)
    squareme.forward(40)
    squareme.left(90)
    squareme.forward(40)
    squareme.left(90)

def drawsquaresizable(squareme, width):
    squareme.fillcolor(randomcolor())  # fill the specified color in the shape
    squareme.begin_fill ()
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)
    squareme.end_fill()


aTurtle = turtle.Turtle()


for i in range(3):
    aTurtle.left(20)
    drawsquare(aTurtle)

# more squares
aTurtle.setposition(0,0)
for i in range(3):
    aTurtle.left(20)
    drawsquaresizable(aTurtle, 20)

aTurtle.setposition(0,0)
for i in range(3):
    aTurtle.left(20)
    drawsquaresizable(aTurtle, 60)


turtle.done()