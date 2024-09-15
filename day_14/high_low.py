import random
from game_data import data
from art import logo,vs
import os

def get_article(word):
    vowel = 'aeiou'
    if word[0].lower() in vowel:
        return 'an'
    else:
        return 'a'

def format_data(acc_data):
    return f"{acc_data['name']}, {get_article(acc_data['description'])} {acc_data['description']} from {acc_data['country']}"

def get_a_or_b(message):
    while True:
        try:
            input_text = input(message).strip().lower()
            if input_text != 'a' and input_text != 'b':
                raise ValueError("Select one 'a' or 'b'")
            return input_text
        except ValueError as e:
            print(e)

def validate(a,b,user_option):
    if user_option == 'a' and a['follower_count']>b['follower_count']:
        return True
    elif user_option == 'b' and a['follower_count']<b['follower_count']:
        return True
    return False

def game():
    game_score = 0
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    while True:    
        print(f"\nCompare A - {format_data(a)}")
        print(vs)
        print(f"Against B - {format_data(b)}")
        user_selection = get_a_or_b("\nWho has more followers. A or B : ")
        os.system('cls')
        if validate(a,b,user_selection):
            game_score += 1
            print(f"You are correct, Current score : {game_score}")
            if user_selection == 'a':
                a = b
                b =  random.choice(data)
                while a == b:
                    b = random.choice(data)
            elif user_selection == 'b':
                b = a
                a = random.choice(data)
                while a == b:
                    a = random.choice(data)
        else:
            print(f"You are wrong. Final score : {game_score} ")
            break
        
print(logo)
game()