import turtle

a = 10
x = 5
y = 5

for i in range(1,11):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for j in range(4):
        turtle.right(90)
        turtle.forward(a)
    a = a + 10
    x = x + 5
    y = y + 5
