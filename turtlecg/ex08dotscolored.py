# -*- coding: utf-8 -*-
import turtle
from colors import randomcolor


seurat = turtle.Turtle()

dot_distance = 20
width = 10
height = 8

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.pencolor(randomcolor())
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)


turtle.done()