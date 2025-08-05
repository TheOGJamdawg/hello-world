import turtle

def drawFractal(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        drawFractal(t, length / 3, level - 1)
        t.left(60)
        drawFractal(t, length / 3, level - 1)
        t.right(120)
        drawFractal(t, length / 3, level - 1)
        t.left(60)
        drawFractal(t, length / 3, level - 1)

def koch(t, length, level):

    for i in range(3):
        drawFractal(t, length, level)
        t.right(120)

t = turtle.Turtle()

koch(t, 300, 2)  # level 2
