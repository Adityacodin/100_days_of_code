import random
from art import logo

def get_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            pass

def get_difficulty(message):
    while True:
        try : 
            diff = input(message).strip().lower()
            if diff != 'easy' and diff != 'hard':
                raise ValueError("Either type in 'easy' or 'hard'")
            return diff
        except ValueError as e:
            print(e)


def play_game(num,atmpts):
    user_guess = None
    while user_guess != num and atmpts != 0:
        print(f"You have {atmpts} attempts remaining to guess the number.")
        user_guess = get_int("Make a guess: ")        
        if user_guess > num:
            print("Too high.\nGuess again.")
        elif user_guess < num:
            print("Too low.\nGuess again.")
        atmpts -= 1
        print("\n"*2)
    if user_guess == num:
        print(f"Yes,you guessed it right.")
    elif atmpts == 0:
        print("You Lose. You ran out of attempts...")
    print(f"The number was {num}")


print(logo)
print("Welcome to the Number Guessing Game")
number = random.randint(1,100)
print("I am thinking of a number between 1 and 100.")
difficulty = get_difficulty("Choose a difficulty. type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
play_game(number,attempts)