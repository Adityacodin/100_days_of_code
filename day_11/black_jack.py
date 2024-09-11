import random
from replit import clear
from art import logo
def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards) 

def calculate_score(cards):
    """calculates score of the cards and returns a value"""
    if sum(cards)==21 and len(cards) == 2:
        # blackjack situation
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_sc,c_sc):
    if u_sc == c_sc:
        return "It's a draw"
    elif c_sc == 0:
        return "Computer has  blackjack, You lose"
    elif u_sc == 0:
        return "You have a blackjack, You win"
    elif u_sc>21:
        return "You went over, You Lose"
    elif c_sc > 21:
        return "Computer went over, You Win"
    else:
        if u_sc > c_sc:
            return "You Win"
        else:
            return "You Lose"

def play_game():
    print(logo)
    user_cards = []
    user_score = -1
    pc_cards = []
    pc_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())

    for i in range(2):
        pc_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_deal ==  'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while pc_score!= 0 and pc_score<17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)
    
    print(f"Your Final Hand: {user_cards}, current score = {user_score}")
    print(f"Computer's Final Hand: {pc_cards}, current score = {pc_score}")
    print(compare(user_score,pc_score))

def main():
    while True:
        play = input("\nDo you want to play a game of blackjack? y/n: ")
        if play == 'y':
            print("\n"*30)
            play_game()
        else:
            break
        
main()