import random
from art import logo

def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    own_deck = []
    pc_deck = []
    for _ in range(2): # 1a ronda de cartas para el usuario
        own_deck.append(random.choice(cards))
    print(f"Your cards are: {own_deck}. Your current score is: {sum(own_deck)}")
    for _ in range(2): # 1a ronda de cartas para la pc
        pc_deck.append(random.choice(cards))
    print(f"Computer's first card is: {pc_deck[0]}")
    return own_deck, pc_deck, cards

def calculate_score(deck):
    # Suma inicial del mazo
    score = sum(deck)
    # Cuenta cuántos Ases (valores de 11) hay en el mazo
    num_aces = deck.count(11)

    # Mientras el score sea mayor a 21 Y tengamos Ases que puedan valer 1,
    # reducimos el valor de un As de 11 a 1 (restamos 10 al score).
    while score > 21 and num_aces > 0:
        score -= 10 # Restamos 10 (convertir 11 en 1)
        num_aces -= 1 # Decrementamos el contador de Ases
    return score


def play_blackjack_game():
    returned_own_deck, returned_pc_deck, returned_cards = blackjack()

    total_own = calculate_score(returned_own_deck)
    total_pc = calculate_score(returned_pc_deck)

    is_game_over = False

    # verificando si alguno obtuvo un blackjack
    if total_own == 21 and len(returned_own_deck) == 2 and total_pc == 21 and len(returned_pc_deck) == 2:
        print("It's a push! Both got Blackjack!")
        is_game_over = True
    elif total_own == 21 and len(returned_own_deck) == 2:
        print("Blackjack! You've won!")
        is_game_over = True
    elif total_pc == 21 and len(returned_pc_deck) == 2:
        print("PC got a Blackjack! You lose.")
        is_game_over = True

    # Solo continuar el juego si NO hay un ganador o empate instantáneo por Blackjack inicial.
    if not is_game_over:

        player_turn_active = True
        while player_turn_active:
            # asegurándose de que la suma del deck del usuario sea al menos 17 antes de darle la opción de si quiere continuar sacando cartas o no
            total_own = calculate_score(returned_own_deck)
            if total_own < 17:
                user_choice = input("Since your current score is lower than 17, another card from the main deck needs to be dealt to you. "
                    "\nType 'c' to continue or 's' to surrender: ").lower().strip()
                while not (user_choice == "c" or user_choice == "s"):
                    print("Invalid input. Try again.")
                    user_choice = input("Since your current score is lower than 17, another card from the main deck needs to be dealt to you. "
                        "\nType 'c' to continue or 's' to surrender: ").lower().strip()
                if user_choice == 's':
                    print("User surrendered. PC won.")
                    return
                elif user_choice == 'c':
                    returned_own_deck.append(random.choice(returned_cards))
                    total_own = calculate_score(returned_own_deck)
                    print(f"Your cards are: {returned_own_deck}. Your current score is: {total_own}")
                    if total_own >= 21:
                        player_turn_active = False

            elif 17 <= total_own < 21:

                # preguntándole al usuario si quiere sacar otra carta o no
                another_card = input("Type 'y' to get another card, or type 'n' to pass: ").lower().strip()
                while not (another_card == "y" or another_card == "n"):
                    print("Invalid input. Try again.")
                    another_card = input("Type 'y' to get another card, or type 'n' to pass: ").lower().strip()
                if another_card == 'y':
                    returned_own_deck.append(random.choice(returned_cards))
                    total_own = calculate_score(returned_own_deck)
                    print(f"Your cards are: {returned_own_deck}. Your current score is: {total_own}")
                    if total_own >= 21:
                        player_turn_active = False
                elif another_card == 'n':
                    print(f"Your final hand is: {returned_own_deck}.")
                    player_turn_active = False
            else:
                player_turn_active = False

        # proceso para pc
        total_own = calculate_score(returned_own_deck)
        if not total_own <= 21: # La PC solo juega si la mano del usuario es válida
            print(f"PC's current hand is: {returned_pc_deck}. PC's current score is: {total_pc}")

            while total_pc < 17:
                returned_pc_deck.append(random.choice(returned_cards))
                total_pc = calculate_score(returned_pc_deck)
                print(f"PC takes a card. PC's hand is {returned_pc_deck}. PC's score is {total_pc}")
                if total_pc >= 21:
                    break
        print(f"PC's final hand is: {returned_pc_deck}. PC's final score is: {total_pc}.")

        # comparando
        total_own = calculate_score(returned_own_deck)
        total_pc = calculate_score(returned_pc_deck)
        # 1. ¿Quién se pasó de 21? (Bust)
        if total_own > 21:
            print("You went over 21. You lose.")
        elif total_pc > 21:
            print("PC went over 21. You've won!")
        # 2. ¿Quién tiene exactamente 21? (No Blackjacks iniciales, ya se manejaron arriba)
        elif total_own == 21:
            print("You got 21! You've won!")
        elif total_pc == 21:
            print("PC got 21! You lose.")
        # 3. Empate (si nadie se ha pasado y nadie tiene 21 exactamente ahora)
        elif total_own == total_pc:
            print("It's a draw!")
        # 4. Comparar puntajes (si nadie se pasó, nadie tiene 21, y no es empate)
        elif total_own > total_pc:
            print("You've gotten closer to 21. You've won!")
        else:
            print("PC got closer to 21. You lose.")



# pregunta del inicio antes de arrancar el programa
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
while not (play == "y" or play == "n"):
    print("Invalid input. Try again.")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()

game_on = True
if play == 'n':
    game_on = False
while game_on:
    print("\n" * 20)
    play_blackjack_game()

    game_on_choice = input("Do you want to play again? Type 'y' or 'n': ").lower().strip()
    while not (game_on_choice == "y" or game_on_choice == "n"):
        print("Invalid input. Try again.")
        game_on_choice = input("Do you want to play again? Type 'y' or 'n': ").lower().strip()
    if game_on_choice == "y":
        game_on = True
    elif game_on == "n":
        game_on = False

print("Goodbye!")
