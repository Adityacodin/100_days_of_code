height = int(input("Whats your height ? :").strip())

if height < 120:
    print("You cannot ride the roller coaster")
else :
    print("You Can ride the roller coaster")
    age = int(input("Age: "))
    amt = 0
    if age <= 12 :
        print("Child tickets are $5 ")
        amt += 5
    elif age>12 and age <=18 :
        print("Youth tickets are $7 ")
        amt += 7
    else :
        print("Adult tickets are $12 ")
        amt += 12
    
    photo_option = input("Do you want a photo of yourself? [y:Yes|n:No]: ")
    if photo_option == 'y':
        amt += 3
    
    print("Total Bill :",amt)