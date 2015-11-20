# -*- coding: utf-8 -*-
import turtle

spiral = turtle.Turtle()

count = 24
for i in range(count):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()