from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    keep_going = "y"
    while keep_going == "y":
        for key in operations:
            print(key)
        op = input("Pick an operation: ").strip()
        while op not in operations:
            print("Invalid input. Try again.")
            op = input("Pick an operation: ").strip()
        second_number = float(input("What's the next number?: "))
        result = operations[op](first_number, second_number)
        print(f"{first_number} {op} {second_number} = {result}")
        keep_going = input(f"Type 'y' to continue calculating with {result}, "
                           f"or type 'n' to start a new calculation: ").lower().strip()

        while not (keep_going == "y" or keep_going == "n"):
            print("Invalid input. Try again.")
            keep_going = input(f"Type 'y' to continue calculating with {result}, "
                               f"or type 'n' to start a new calculation: ").lower().strip()

        if keep_going == "y":
            first_number = result
        print("\n" * 20)


restart = True
while restart:
    calculator()
