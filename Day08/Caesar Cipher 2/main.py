alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {output_text}")

## -----

# def caesar(new_direction ,original_text, shift_amount):
#     if new_direction == "encode":
#         cipher_text = ""
#         for letter in original_text:
#             if letter in alphabet:
#                 shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#                 cipher_text += alphabet[shifted_position]
#             else:
#                 cipher_text += letter
#         print(f"Here is the encoded result: {cipher_text}")
#     elif new_direction == "decode":
#         output_text = ""
#         for letter in original_text:
#             if letter in alphabet:
#                 shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
#                 output_text += alphabet[shifted_position]
#             else:
#                 output_text += letter
#         print(f"Here is the decoded result: {output_text}")
#
# caesar(direction, text, shift)

def caesar(encode_or_decode ,original_text, shift_amount):
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

caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
