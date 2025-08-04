#-------------------------------------------------------------------------------
# Author:      Erick Rico
# Created:     03/08/2025
#-------------------------------------------------------------------------------

import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")
all_states = df["state"].tolist() # Creating a list of all state names
guessed_states = [] # List to save all the guessed states

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Main part of the game
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title().strip()

    # Option to exit the game
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Finding state coordinates
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_row = df[df["state"] == answer_state]
        x_coord = int(state_row["x"].item())
        y_coord = int(state_row["y"].item())

        # Moving the turtle and writing the name of the state
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_coord, y_coord)
        t.write(answer_state)

    if len(guessed_states) == 50:
        game_is_on = False
        print("Congrats! You've guessed the 50 States!")
        break