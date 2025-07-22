import random
import art
from game_data import data

def get_choice(prompt_message, valid_options):
    while True:
        letter_choice = input(prompt_message).upper().strip()
        if letter_choice in valid_options:
            return letter_choice
        else:
            print(f"Invalid input. Please type one of these: {", ".join(valid_options)}")


def main_game():
    print(art.logo)

    score = 0
    a_choice = random.choice(data)
    game_active = True
    while game_active:

        print(f"Compare A: {a_choice["name"]}, a {a_choice["description"]}, from {a_choice["country"]}.")

        print(art.vs)

        b_choice = random.choice(data)
        while a_choice == b_choice:
            b_choice = random.choice(data)
        print(f"Against B: {b_choice["name"]}, a {b_choice["description"]}, from {b_choice["country"]}.")

        if a_choice["follower_count"] > b_choice["follower_count"]:
            correct_answer = 'A'
        else:
            correct_answer = 'B'

        letter_options = ['A', 'B']
        user_guess = get_choice("Who has more followers? Select 'A' or 'B': ", letter_options)

        if user_guess == correct_answer:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            if correct_answer == 'A':
                a_choice = b_choice
        else:
            print("\n" * 20)
            print(f"Sorry, that's wrong! Your final score is: {score}")
            game_active = False

if __name__ == "__main__":
    main_game()
