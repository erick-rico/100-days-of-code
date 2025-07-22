from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of an integer number between 1 and 100.")
number = random.randint(1,100)


choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
while not (choice == 'easy' or choice == 'hard'):
    print("Invalid input. Try again.")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

if choice == 'easy':
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")
    guess = float(input("Make a guess: "))

    while not guess == number:
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The answer was {number}. Refresh the page to run again.")
            break

        elif attempts >= 1:
            if guess > number:
                print("Too high.")
                print(f"You have {attempts} remaining to guess the number.")
                guess = float(input("Make a guess: "))

            elif guess < number:
                print("Too low.")
                print(f"You have {attempts} remaining to guess the number.")
                guess = float(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")

elif choice == 'hard':
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")
    guess = float(input("Make a guess: "))

    while not guess == number:
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The answer was {number}. Refresh the page to run again.")
            break

        elif attempts >= 1:
            if guess > number:
                print("Too high.")
                print(f"You have {attempts} remaining to guess the number.")
                guess = float(input("Make a guess: "))

            elif guess < number:
                print("Too low.")
                print(f"You have {attempts} remaining to guess the number.")
                guess = float(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")


