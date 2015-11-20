# -*- coding: utf-8 -*-
import turtle

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess's Spiral")

tess = turtle.Turtle()
tess.shape("turtle")          # a turtle shape can be “arrow”, “turtle”,
                              #  “circle”, “square”, “triangle”, “classic”
tess.color("blue")

tess.penup()                  # set pen up
distance = 30
for i in range(40):
    tess.stamp()              # leave an impression on the canvas
    distance += 2             # increase the size on every iteration
    tess.forward(distance)    # move tess along
    tess.right(24)            # and turn her


turtle.done()