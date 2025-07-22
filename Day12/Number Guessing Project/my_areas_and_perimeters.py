# variables globales
PI = 3.14159

# elección
def get_choice(prompt_message, valid_options):
    while True:
        user_input = input(prompt_message).lower().strip()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please type one of these: {", ".join(valid_options)}")

# numero positivo
def get_positive_number(prompt_message):
    while True:
        try:
            number = float(input(prompt_message))
            if number < 0:
                print("The side cannot be a negative value. Please enter a positive one.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# cálculos para círculo
def circle_area(length):
    radius = length / 2
    return f"The circle area is {(PI * radius ** 2):.2f} square units."

def circle_perimeter(length):
    radius = length / 2
    return f"The circle perimeter is {(2 * PI * radius):.2f} linear units."

# cálculos para cuadrado
def square_area(length):
    return f"The square area is {(length * length):.2f} square units."

def square_perimeter(length):
    return f"The square perimeter is {(length * 4):.2f} linear units."

# función principal
def main_calculator():
    print("Welcome to the Area and Perimeter calculator for Circles and Squares!")
    figure_options = ["circle", "square"]
    figure_choice = get_choice("Which geometric figure would you like to calculate? "
                               "Type 'circle' or 'square': ", figure_options)
    print(f"You chose: {figure_choice}")

    calculation_options = ["area", "perimeter"]
    calculation_choice = get_choice("What would you like to calculate? "
                               "Type 'area' or 'perimeter': ", calculation_options)
    print(f"You chose: {calculation_choice}")

    positive_number = get_positive_number("Enter the side or diameter of the figure: ")
    print(f"The length is: {positive_number}")

    if figure_choice == 'circle':
        if calculation_choice == 'area':
            print(circle_area(positive_number))
        else:
            print(circle_perimeter(positive_number))
    elif figure_choice == 'square':
        if calculation_choice == 'area':
            print(square_area(positive_number))
        else:
            print(square_perimeter(positive_number))

if __name__ == "__main__":
    main_calculator()

