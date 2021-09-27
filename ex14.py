import turtle as tr
import math

def star(n, r):
    tr.penup()
    tr.goto(r, 0)
    tr.pendown()
    for i in range(1, n + 1):
        tr.goto(r * math.cos(math.pi * (1 - 1 / n) * i),
                r * math.sin(math.pi * (1 - 1 / n) * i))

r = 60
n = int(input())
star(n, r)
