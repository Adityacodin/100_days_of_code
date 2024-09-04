import random

def print_choice(x):
    if x == "ROCK":
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif x == "PAPER":
        print("     _______")
        print("---'   ____)____")
        print("           ______)")
        print("           _______)")
        print("          _______)")
        print(" ---.__________)")
    elif x == "SCISSORS":
        print("     _______")
        print("---'   ____)____")
        print("           ______)")
        print("           _______)")
        print("       (____)")
        print(" ---.__(___)")

userip = int(input("WHAT DO YOU CHOOSE ? 0-ROCK,1-PAPER,2-PAPER "))
choice_list = ["ROCK","PAPER","SCISSORS"]
print("YOU CHOSE : ")
print_choice(choice_list[userip])

print("\nCOMPUTER CHOSE : ")
computerip = random.randint(0,2)
print_choice(choice_list[computerip])

if userip == computerip:
    print("DRAW")
if userip == 0 and computerip == 1:
    print("COMPUTER WON")
if userip == 0 and computerip == 2:
    print("YOU WON")
if userip == 1 and computerip == 0:
    print("YOU WON")
if userip == 1 and computerip == 2:
    print("COMPUTER WON")
if userip == 2 and computerip == 0:
    print("COMPUTER WON")
if userip == 2 and computerip == 1:
    print("YOU WON")




