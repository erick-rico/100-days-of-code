from art import logo1

LOW_TIP = 10
MEDIUM_TIP = 12
HIGH_TIP = 15

# obteniendo y validando la cuenta total
def get_total_bill():
    print(logo1)
    print("Welcome to the tip calculator!")

    while True:
        try:
            bill_str = input("What was the total bill? $")
            bill = float(bill_str)
            if bill < 0:
                print("The bill cannot be negative. Please enter a positive number.")
                continue
            return bill
        except ValueError:
            print("Invalid input. Please enter a valid number for the bill (e.g., 124.56).")


# obteniendo y validando el porcentaje del tip
def get_tip_percentage():
    while True:
        try:
            tip_str = input(f"What percentage tip would you like to give? ({LOW_TIP}, {MEDIUM_TIP} or {HIGH_TIP}) ")
            tip = float(tip_str)
            if tip in [LOW_TIP, MEDIUM_TIP, HIGH_TIP]:
                return tip
            else:
                print(f"Invalid input. Please enter {LOW_TIP}, {MEDIUM_TIP} or {HIGH_TIP}.")
        except ValueError:
            print("Invalid input. Please enter a whole number for the tip percentage.")


# obteniendo y validando número de personas
def get_num_people():
    while True:
        try:
            people_str = input("How many people to split the bill? ")
            people = int(people_str)
            if people <= 0 or people == float:
                print("The number of people must be at least 1. Please enter a positive whole number.")
                continue
            return people
        except ValueError:
            print("Invalid input. Please enter a valid whole number for the number of people.")


# función orquestando el programa
def calculate_final_bill():
    total = get_total_bill()
    percentage = get_tip_percentage()
    people = get_num_people()

    final_amount_per_person = (total * (1 + percentage / 100)) / people
    print(f"Each person should pay: ${final_amount_per_person:.2f}")


if __name__ == "__main__":
    calculate_final_bill()


