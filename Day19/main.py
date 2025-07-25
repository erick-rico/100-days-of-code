from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which color will win the race? Enter the color: ").lower().strip()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
turtles = []

while user_bet not in colors:
    print(f"Invalid color. Try one of these: {", ".join(colors)}.")
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which color will win the race? Enter the color: ").lower().strip()

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_coordinates[turtle])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230: # turtle object is 40x40, so 250 - (40 / 2) = 230
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle has won the race!")
            else:
                print(f"You've lost! {winning_color} turtle has won the race!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
