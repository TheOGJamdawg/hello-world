import turtle
import math

def drawCircle(t, x, y, radius):
    t.penup()
    t.goto(x + radius, y)
    t.pendown()
    movement = (2.0 * math.pi * radius) / 120

    for i in range(120):
        t.forward(movement)
        t.left(3) #3 degree change every step

t = turtle.Turtle()

drawCircle(t, 0, 0, 100)
