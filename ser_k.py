import turtle


def ser(a):
    if a < 50:
        a = a / 3
        turtle.penup()
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.begin_fill()
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.end_fill()
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(180)
        turtle.pendown()
        return

    a = a / 3
    ser(a)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.left(180)
    turtle.forward(a * 2)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.forward(a * 2)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.left(180)
    turtle.forward(a * 2)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

    ser(a)

    turtle.penup()
    turtle.left(180)
    turtle.forward(a * 2)
    turtle.left(90)
    turtle.forward(a * 2)
    turtle.left(90)
    turtle.pendown()



turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

a = 200
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
ser(a)

turtle.exitonclick()
