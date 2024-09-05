import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!,''@','#','$','%','^','&','*','(',')']

print("Welcome to PyPassword Generator")
no_of_letters = int(input("How many letters would you like in your password: "))
no_of_numbers = int(input("How many numbers would you like in your password: "))
no_of_symbols = int(input("How many symbols would you like in your password: "))

password = []
for i in range(0,no_of_letters):
    password.append(random.choice(letters))

for i in range(0,no_of_numbers):
    ind = random.randint(0,len(password))
    password.insert(ind,random.choice(numbers))
    
for i in range(0,no_of_symbols):
    ind = random.randint(0,len(password))
    password.insert(ind,random.choice(symbols))

password_as_string = ''
for characters in password:
    password_as_string += characters


print(password_as_string)