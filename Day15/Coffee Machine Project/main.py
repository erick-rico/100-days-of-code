MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_choice(user_prompt, valid_options):
    """Checks if the option input by the user is valid."""
    while True:
        user_choice = input(user_prompt).lower().strip()
        if user_choice in valid_options:
            return user_choice
        else:
            print(f"Invalid input. Please type one of these: {", ".join(valid_options)}")

def get_num_coins(user_prompt, type_of_coin):
    """Returns the number of a specifically inserted coin."""
    while True:
        try:
            coins_str = input(user_prompt)
            coins = int(coins_str)
            if coins < 0:
                print(f"The number of {type_of_coin} must be at least 0. Please enter 0 or a positive whole number.")
                continue
            return coins
        except ValueError:
            print(f"Invalid input. Please enter a valid number for the number of {type_of_coin} you will pay with.")

def sum_coins(num_quarters, num_dimes, num_nickles, num_pennies):
    """Returns the total amount of money inserted as coins."""
    quarters_value = 0.25 * num_quarters
    dimes_value = 0.10 * num_dimes
    nickles_value = 0.05 * num_nickles
    pennies_value = 0.01 * num_pennies
    total_paid = quarters_value + dimes_value + nickles_value + pennies_value
    return total_paid

# Verificar Suficiencia de Dinero
def check_money(paid_money, drink_cost):
    if paid_money < drink_cost:
        shortfall = drink_cost - paid_money
        print(f"We're sorry. You're missing ${shortfall:.2f}.")
        return False
    else:
        change = paid_money - drink_cost
        print(f"Here's your change: {change:.2f}")
        return True

# Verificar Suficiencia de Recursos
def check_resources(drink_ingredients):
    for ingredient_name, required_amount in drink_ingredients.items():
        if resources[ingredient_name] < required_amount:
            print(f"We're sorry. We're out of {ingredient_name}.")
            return False
    return True

# Realizar la Transacción y Suministrar Café
def make_coffee(drink_name, drink_ingredients, drink_cost):
    for ingredient_name, required_amount in drink_ingredients.items():
        resources[ingredient_name] -= required_amount
    resources["money"] = resources.get("money", 0.0) + drink_cost

    print(f"Here's your {drink_name} ☕. Enjoy!")

# Flujo principal
def main():
    turn_on = True
    while turn_on:
        word_options = ["espresso", "latte", "cappuccino", "report", "off"]
        user_input = get_choice("What would you like? (espresso/latte/cappuccino): ", word_options)

        if user_input == "off":
            turn_on = False
            print("Turning off the coffee machine. Goodbye!")
            continue
        elif user_input == "report":
            print("--- Current Resources ---")
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${resources.get("money", 0.0):.2f}")
            continue

        # Verificando que el usuario eliga una bebida
        drink_details = MENU.get(user_input)
        if not drink_details:
            print("Error: Beverage details not found.")
            continue

        # Obtener la Información de la Bebida Elegida
        drink_ingredients = drink_details["ingredients"]
        if not check_resources(drink_ingredients):
            continue
        drink_cost = drink_details["cost"]
        print(f"Your drink costs: ${drink_cost:.2f}")

        print("Please insert coins.")
        num_quarters = get_num_coins(f"How many quarters?: ", "quarters")
        num_dimes = get_num_coins(f"How many dimes?: ", "dimes")
        num_nickles = get_num_coins(f"How many nickles?: ", "nickles")
        num_pennies = get_num_coins(f"How many pennies?: ", "pennies")

        total_sum = sum_coins(num_quarters, num_dimes, num_nickles, num_pennies)
        print(f"You inserted: ${total_sum:.2f}")

        if not check_money(total_sum, drink_cost):
            print("Money refunded.")
            continue

        make_coffee(user_input, drink_ingredients, drink_cost)

if __name__ == "__main__":
    main()
