print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final_bill = bill * (1 + tip / 100) / people

print(f"Each person should pay: ${round(final_bill,2)}")


