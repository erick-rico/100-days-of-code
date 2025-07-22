import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


while True:
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if user_choice == "0":
        print(rock)
        break
    elif user_choice == "1":
        print(paper)
        break
    elif user_choice == "2":
        print(scissors)
        break
    else:
        print("Invalid input. Choose 0, 1 or 2.")


choices = [rock, paper, scissors]
computer_choice = random.choice(choices)
print(f"Computer chose:\n{computer_choice}")

if user_choice == "0" and computer_choice == rock:
    print("It's a tie. Play again.")
elif user_choice == "0" and computer_choice == paper:
    print("You lose. Paper beats Rock.")
elif user_choice == "0" and computer_choice == scissors:
    print("You win. Rock beats Scissors.")
elif user_choice == "1" and computer_choice == rock:
    print("You win. Paper beats Rock.")
elif user_choice == "1" and computer_choice == paper:
    print("It's a tie. Play again.")
elif user_choice == "1" and computer_choice == scissors:
    print("You lose. Scissors beat Paper.")
elif user_choice == "2" and computer_choice == rock:
    print("You lose. Rock beats Scissors.")
elif user_choice == "2" and computer_choice == paper:
    print("You win. Scissors beat Paper.")
elif user_choice == "2" and computer_choice == scissors:
    print("It's a tie. Play again.")