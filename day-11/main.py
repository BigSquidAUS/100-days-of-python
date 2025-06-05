import art
import random
print(art.logo)

players_cards = []
players_score = 0
computers_cards = []
computers_score = 0

def deal_cards(card_list, number_to_deal):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if card_list == players_cards:
        print(f"\nPlayer is dealt {number_to_deal} card(s).")
    else:
        print(f"\nDealer is dealt {number_to_deal} card(s)")

    for this_card in range(number_to_deal):
        card_list.append(random.choice(cards))

def calculate_score(card_list):
    total = sum(card_list)
    if total > 21 and 11 in card_list: #If score is over 21 and there is an Ace in your hand.
        for i, card in enumerate(card_list): #Loop through all the cards in your hand.
            if card == 11: #Find the Ace.
                card_list[i] = 1 #Set the Ace = 1
                print("Ace reduced")
                total = sum(card_list)
                return total
    total = sum(card_list)
    return total

def check_game_over(p_score = 0, c_score = 0, end_game = False):
    if end_game:
        return True

    if p_score > 21:
        #print(f"Dealer Wins! Player went bust with score: {p_score}")
        return True
    elif c_score > 21:
        #print(f"Player Wins! Dealer went bust with score: {c_score}")
        return True
    else:
        return False

def print_cards_score(card_list):
    total = calculate_score(card_list)
    if card_list == players_cards:
        print(f"Your cards {players_cards}, current score: {total}\n")
    else:
        print(f"Computers card(s) {computers_cards}, current score: {total}\n")

def hit_or_stay():
    prompt = input("Type 'y' for another card, type 'n' to pass: ")
    if prompt.lower() in ("y","yes"):
        return True
    else:
        return False

play_game = True

while play_game:
    calculate_score(players_cards)
    calculate_score(computers_cards)

    deal_cards(players_cards,2)
    print_cards_score(players_cards)

    deal_cards(computers_cards,1)
    print_cards_score(computers_cards)

    end_the_game = False

    while not check_game_over(players_score, computers_score, end_the_game):
        if hit_or_stay(): # Player chose to 'Hit' (Continue)
            deal_cards(players_cards,1)
            print_cards_score(players_cards)
            players_score = calculate_score(players_cards)
            print_cards_score(computers_cards)
            computers_score = calculate_score(computers_cards)
        else: # Player chose to 'Stay' with the cards dealt.
            print("Player stays.")

            while not check_game_over(players_score, computers_score, end_the_game):
                if calculate_score(computers_cards) < calculate_score(players_cards):
                    deal_cards(computers_cards,1)
                    check_game_over(players_score, computers_score, end_the_game)
                    computers_score = calculate_score(computers_cards)
                    print_cards_score(computers_cards)


                elif calculate_score(computers_cards) > calculate_score(players_cards):
                    check_game_over(players_score, computers_score, end_the_game)
                    print("Computer wins")
                    computers_score = calculate_score(computers_cards)
                    end_the_game = True

                while calculate_score(computers_cards) < 17:
                    deal_cards(computers_cards,1)
                    check_game_over(players_score, computers_score, end_the_game)
                    computers_score = calculate_score(computers_cards)
                    print_cards_score(computers_cards)

                end_the_game = True

    if players_score > computers_score and players_score <= 21:
        print(f"**Player won with a score of {players_score}.**")
    elif computers_score > players_score and computers_score <= 21:
        print(f"**Dealer won with a score of {computers_score}.**")
    elif computers_score == players_score:
        print(f"This is a draw. Both players scored: P: {players_score} D: {computers_score}")

    if computers_score > 21:
        print(f"Player wins. Dealer busts with {computers_score}.")
    elif players_score > 21:
        print(f"Dealer wins. Player busts with {players_score}.")

    print("Game over.")
    play_again = input("Play again? (Y/N)")

    if play_again.lower() in ("y","yes"):
        players_cards = []
        computers_cards = []
        players_score = 0
        computers_score = 0
        play_game = True
    else:
        play_game = False
