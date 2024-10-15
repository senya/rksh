import turtle


def ser(a):
    if a < 20:
        turtle.begin_fill()
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(a)
        turtle.left(120)
        turtle.end_fill()
        return

    ser(a / 2)

    turtle.penup()
    turtle.forward(a / 2)
    turtle.pendown()

    ser(a / 2)

    turtle.penup()
    turtle.left(120)
    turtle.forward(a / 2)
    turtle.right(120)
    turtle.pendown()

    ser(a / 2)

    turtle.penup()
    turtle.right(120)
    turtle.forward(a / 2)
    turtle.left(120)
    turtle.pendown()


turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

ser(200)

turtle.exitonclick()
