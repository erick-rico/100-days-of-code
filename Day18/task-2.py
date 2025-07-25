# Challenge 2

from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.pendown()  # Draw the dash
    tim.forward(10)
    tim.penup()  # Create the gap
    tim.forward(10)

screen = Screen()
screen.exitonclick()