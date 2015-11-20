# -*- coding: utf-8 -*-
# We can rotate the turtle in order to draw more interesting figures.
import turtle

box1Px = 20
smart = turtle.Turtle()

# Loop 4 times.
for i in range(4):
    smart.forward(box1Px)
    smart.right(90)

# Now move forward with some more pixels in several steps

stepPx = 5
manyBoxPx = box1Px
manyBoxPx += stepPx

smart.forward(manyBoxPx)
smart.right(-270)

for i in range(40):
    smart.forward(manyBoxPx)
    smart.right(90)
    manyBoxPx += stepPx


turtle.done()