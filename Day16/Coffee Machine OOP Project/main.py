from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower().strip()
    if choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



# otra forma a partir del else:
        # drink = menu.find_drink(choice)
        # if drink is None:
        #     continue
        #
        # if not coffee_maker.is_resource_sufficient(drink):
        #     continue
        #
        # if money_machine.make_payment(drink.cost):
        #     coffee_maker.make_coffee(drink)



