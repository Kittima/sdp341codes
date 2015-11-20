# -*- coding: utf-8 -*-
import turtle


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
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)
    squareme.forward(width)
    squareme.left(90)


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