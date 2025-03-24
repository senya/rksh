from turtle import *


def koh(n):
    if n == 0:
        forward(20)
        return

    koh(n - 1)
    left(60)
    koh(n - 1)
    right(120)
    koh(n - 1)
    left(60)
    koh(n - 1)


speed(0)
penup()
goto(-200, 0)
pendown()

koh(4)

exitonclick()
