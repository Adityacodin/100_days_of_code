print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
ans = input("You are at a cross road, will you go left or right?")

if ans == 'right':
    print("Game Over")
elif ans == 'left':
    ans = input("You arrived at a lake, wait for boat or swim ?")
    if ans == 'swim':
        print("Game Over")
    elif ans == 'wait':
        ans = input("You arrived at the castle, there are three door R,Y and B, which to choose ? ")
        if ans == 'R':
            print("Fire , Game Over")
        if ans == 'Y':
            print("You Win !!!")
        if ans == 'B':
            print("Crocodiles , Game Over")
            