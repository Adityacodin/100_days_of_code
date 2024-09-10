from art import logo

print(logo)
print()

def find_highest_bidder(bidding_list):
    highest_bid = 0
    winner = None
    for key in bidders:
        if highest_bid < bidders[key]:
            highest_bid = bidders[key]
            winner = key
    print(f"{winner} has won with the bid of {highest_bid}$")


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
        find_highest_bidder(bidders)