# TODO-1: Import and print the logo from art.py when the program starts.
from types import get_original_bases

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")



# TODO-3: Can you figure out a way to restart the cipher program?





go_again = "yes"
while go_again == "yes":
    direction = ""
    while not (direction == "encode" or direction == "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
        if direction != "encode" and  direction != "decode":
            print("Invalid input. Try again")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower().strip()
print("Goodbye!")

