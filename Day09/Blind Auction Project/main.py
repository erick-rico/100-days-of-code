# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# import os
# os.system("cls")

import art

print(art.logo)

bidders = "yes"
bids = {}
while bidders == "yes":
    name = input("What is your name?: ").strip()
    price = float(input("What is your bid?: $").strip())
    bids[name] = price
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()
    while not (bidders == "yes" or bidders == "no"):
        print("Invalid input. Try again.")
        bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()
    print("\n" * 100)

result = max(bids.items(), key = lambda x: x[1])
print(f"The winner is {result[0]} with a bid of ${result[1]}")

# se podría agregar un bloque try-except para manejar un ValueError por si no se ingresa un numero en price
# Un bucle que se repita hasta que obtengas un precio válido
# valid_price_entered = False
# while not valid_price_entered:
#     try:
#         # Intenta obtener el precio
#         price_input = input("What is your bid?: $").strip()
#         price = float(price_input)
#         # Si llegas aquí, ¡el precio es válido!
#         valid_price_entered = True # Cambia la bandera para salir del bucle de validación
#     except ValueError:
#         # Si llegas aquí, hubo un error al convertir a float
#         print("Invalid input. Please enter a valid number for your bid.")
#         # La bandera sigue siendo False, así que el bucle se repite


# además, se podría hacer algo como esto:
# 1. Encontrar la puja máxima (solo el número)
#    Puedes obtener todos los valores del diccionario y usar max() en ellos.

# 2. Crear una lista vacía para almacenar a los ganadores empatados.

# 3. Recorrer cada 'nombre' y 'puja' en tu diccionario 'bids'.
#    Si la 'puja' de ese 'nombre' es igual a la puja máxima que encontraste en el paso 1,
#    añade el 'nombre' a tu lista de ganadores empatados.

# 4. Imprimir la lista de ganadores, o un mensaje especial si la lista tiene más de un elemento.