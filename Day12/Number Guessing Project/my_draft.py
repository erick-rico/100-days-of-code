from art import logo
import random

# --- Function to handle a single round of guessing ---
def play_game(attempts, secret_number):
    """
    Plays a single round of the number guessing game.

    Args:
        attempts (int): The number of attempts the player gets.
        secret_number (int): The number to be guessed.
    """
    print(f"You have {attempts} remaining to guess the number.")

    # Initialize guess outside the loop to enter the loop
    guess = 0 # Use 0 or any non-matching number initially

    # Keep looping as long as attempts are left AND the guess is incorrect
    while attempts > 0 and guess != secret_number:
        try: # Use a try-except block to handle non-numeric input gracefully
            guess = int(input("Make a guess: ")) # Use int() since it's an integer game
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Skip the rest of this loop iteration and ask for input again

        if guess == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            return # Exit the function because the game is won

        # If guess is incorrect, decrement attempts and provide feedback
        attempts -= 1
        if guess > secret_number:
            print("Too high.")
        elif guess < secret_number:
            print("Too low.")

        # Provide feedback on remaining attempts if game isn't over
        if attempts > 0:
            print(f"You have {attempts} remaining to guess the number.")
        else:
            print(f"You've run out of guesses. The answer was {secret_number}.")
            # No need for 'break' here, as 'attempts > 0' condition in while loop will become false


# --- Main game setup ---
def main_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of an integer number between 1 and 100.")

    # The number should be generated once per game instance
    number = random.randint(1, 100)

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    while not (choice == 'easy' or choice == 'hard'):
        print("Invalid input. Try again.")
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

    if choice == 'easy':
        initial_attempts = 10
    else: # choice == 'hard'
        initial_attempts = 5

    # Call the generic game logic function with the chosen attempts and the secret number
    play_game(initial_attempts, number)

# Run the main game function when the script is executed
if __name__ == "__main__":
    main_game()