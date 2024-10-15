import turtle


def koh(n):
    if n == 0:
        turtle.forward(5)
        return

    n -= 1

    koh(n)
    turtle.left(90)
    koh(n)
    turtle.right(90)
    koh(n)
    turtle.right(90)
    koh(n)
    koh(n)
    turtle.left(90)
    koh(n)
    turtle.left(90)
    koh(n)
    turtle.right(90)
    koh(n)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

koh(3)

turtle.exitonclick()
