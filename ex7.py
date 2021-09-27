import turtle
import math

phi = 0
for phi in range(10000):
    x = 1 * (phi / 10) * math.cos(phi / 10)
    y = 1 * (phi / 10) * math.sin(phi / 10)
    turtle.goto(x,y)
