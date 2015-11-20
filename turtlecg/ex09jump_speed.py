# -*- coding: utf-8 -*-
import turtle

ninja = turtle.Turtle()
'''
If you set the speed to 10, the turtle will go really fast.
If you set the speed to 1, the turtle will go really slow (which is useful
  for trying to understand how some complicated thing is being drawn).
If you set the speed to zero, however, the turtle will go at warpspeed and
  will draw as fast as it can.
'''
ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    '''
    This sets the turtle’s position to the coordinates (0, 0).
      (0, 0) is located at the center of the screen ehere
      the turtle first started.
    Note that you need to make sure the turtle’s pen is up,
      otherwise it will draw a line back to that.
    '''
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)


turtle.done()