import turtle


def pif(a):
    if a < 5:
        turtle.forward(a)
        return

    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)

    turtle.left(180)
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()
    turtle.right(45)

    b = a / (2 ** 0.5)
    pif(b)
    turtle.right(90)
    pif(b)
    turtle.right(45)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()
    turtle.left(90)

turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

pif(12)

turtle.exitonclick()
