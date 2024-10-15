from turtle import *

def square(a):
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)


square(10)

penup()
forward(20)
pendown()

square(50)

penup()
left(45)
forward(150)
pendown()

square(30)

exitonclick()
