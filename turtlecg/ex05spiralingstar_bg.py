# -*- coding: utf-8 -*-
import turtle

spiral = turtle.Turtle()

wn = turtle.Screen()  # get the Screen object
wn.bgcolor("gray")

spiral.pensize(4)

count = 40
for i in range(count):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()