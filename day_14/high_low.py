import random
from game_data import data
from art import logo,vs

def get_article(word):
    vowel = 'aeiou'
    if word[0].lower() in vowel:
        return 'an'
    else:
        return 'a'

def get_a_or_b(message):
    while True:
        try:
            input_text = input(message).strip().lower()
            if input_text != 'a' and input_text != 'b':
                raise ValueError("Select one 'a' or 'b'")
            return input_text
        except ValueError as e:
            print(e)


def game():
    game_score = 0
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    while True:    
        print(f"\nCompare A - {a['name']}, {get_article(a['description'])} {a['description']} from {a['country']}")
        print(vs)
        print(f"Against B - {b['name']}, {get_article(b['description'])} {b['description']} from {b['country']}")
        user_selection = get_a_or_b("\nWho has more followers. A or B : ")
        print("\n"*30)
        if user_selection == 'a' and a['follower_count']>b['follower_count']:
            game_score += 1
            print(f"You are correct. Current score : {game_score}")
            a = b
            b = random.choice(data)
            while a == b:
                b = random.choice(data)
        elif user_selection == 'b' and a['follower_count']<b['follower_count']:
            game_score += 1
            print(f"You are correct. Current score : {game_score}")
            b = a
            a = random.choice(data)
            while a == b:
                a = random.choice(data)
        else:
            print(f"You are wrong. Final score : {game_score} ")
            break

print(logo)
game()