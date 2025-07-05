import random
from art import logo

player_card = []
dealer_card = []

cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

def welcome():
    logo
    print("Welcome to Blackjack!")

def get_player_card():
    random_values = random.choices(list(cards.values()), k=2)

    total = 0
    for card in random_values:
        total += card

    player_card.extend(random_values)

    return random_values , total
    

def get_dealer_card():
    random_values = random.choices(list(cards.values()), k=2)

    total = 0
    for card in random_values:
        total += card

    dealer_card.extend(random_values)

    return random_values , total

def another_card():
    while True:
        ask = input('Do you want to draw another card? Yes or No: ').lower()

        if ask == "yes":
            new_card = random.choice(list(cards.values()))
            player_card.append(new_card)
            total = sum(player_card)

            print(f"You drew: {new_card}")
            print(f"Your cards: {player_card}, Total : {total}")

            if total > 21:
                print("You Lost! Bust 💥")
                return False
            elif total == 21:
                print("Blackjack! 🎉")
                return True
        elif ask == "no":
            total = sum(player_card)
            print(f"You stopped. Final hand: {player_card}, Total : {total}")
            return True
        else:
            print("Please type Yes or No")

def dealer_turn():
    while sum(dealer_card) < 17:
        new_card = random.choice(list(cards.values()))
        dealer_card.append(new_card)
        total = sum(dealer_card)

        if total > 21:
            print(f"You Won! Dealer draws out total of {total}")
            break
        elif total == 21:
            print(f"You Lost! Dealer Blackjack!")
            break

def compare_total():
    dealer_total = sum(dealer_card)
    player_total = sum(player_card)

    
    if dealer_total > 21:
        print("You Won! Dealer busts 💥")
    elif dealer_total == 21:
        print("You Lost! Dealer got Blackjack 🃏")
    else:
        if dealer_total > player_total:
            print("You Lost! Dealer has higher total.")
        elif dealer_total < player_total:
            print("You Won! You have higher total.")
        else:
            print("It's a Draw! 🤝")
    

def main():
    while True:
        player_card.clear()
        dealer_card.clear()

        welcome()
        player_cards , player_total = get_player_card()
        dealer_cards = get_dealer_card()

        print(f"Your cards: {player_cards}, Total: {player_total}")
        print(f"Dealer cards: {dealer_cards[0][1]}")

        continue_game = another_card()

        if continue_game and sum(player_card) <= 21:
            dealer_turn()
            compare_total()
        
        play_again = input("Play again? Yes or No: ").lower()
        if play_again != "yes":
            print("Thanks for playing Blackjack!")
            break
           
if __name__ == "__main__":
    main()
