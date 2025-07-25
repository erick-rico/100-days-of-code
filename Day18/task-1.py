from turtle import Turtle, Screen

tim = Turtle()

# Challenge 1
while True:
    tim.right(90)
    tim.forward(100)
    if abs(tim.pos()) < 1:
        break

# otra forma:
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)


screen = Screen()
screen.exitonclick()