import random

word_list = ["camel","elephant","lion","baboon"]

# randomly choose a word and assign it to a variable
selected_word  = random.choice(word_list)
print(selected_word)

# ask the user to guess a letter and convert it to lowercase
user_letter = input("Guess a letter : ").strip().lower()

# check if the the letter matches with any of the letters in the word
# if it does then print "right" else "wrong"

for char in selected_word :
    if char == user_letter : 
        print("Right")
    else:
        print("Wrong")