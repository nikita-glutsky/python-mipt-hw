import turtle
import math

def npoly(n, r):
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    for i in range(n):
        turtle.left(360 / n)
        turtle.forward(2 * r * math.sin(math.pi / n))

r = 15
n = 3
turtle.left(90)

for i in range(10):
    npoly(n, r)
    r += 15
    n += 1

    
