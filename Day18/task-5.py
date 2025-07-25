# Challenge 5

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for angle in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(angle)
    tim.circle(100)

screen = t.Screen()
screen.exitonclick()