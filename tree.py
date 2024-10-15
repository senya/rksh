from turtle import *


def tree(a):
    if a < 20:
        color('green')
        width(a / 4)
        forward(a)
        left(180)
        forward(a)
        left(180)
        return

    a *= 0.7
    color('brown')
    width(a * 0.1)
    forward(a)
    right(60)
    tree(a)
    left(100)
    tree(a)
    right(40)

    penup()
    backward(a)
    pendown()


speed(0)
left(90)
tree(200)

exitonclick()
