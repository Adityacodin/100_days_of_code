from art import logo

bidders = {}
cont = True
to_continue = None

while cont:
    name = input("What's your name: ")
    price = int(input("Enter your bid: $"))
    bidders[name]=price

    to_continue = input("Do you wish to continue ? (yes/no): ")
    print("\n" * 100)
    if to_continue.lower() == 'no':
        cont = False

maxi = 0
winner = None
for key in bidders:
    if maxi < bidders[key]:
        maxi = bidders[key]
        winner = key
    

print(f"{winner} has won with the bid of {maxi}$")