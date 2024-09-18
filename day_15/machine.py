from coffee import coffee_info

machine_water = 500
machine_milk = 500
machine_coffee = 50
machine_money = 0

def off_the_machine():
    exit()

def show_report():
    global machine_water,machine_coffee,machine_milk
    print(f"Water: {machine_water}ml")
    print(f"Milk: {machine_milk}ml")
    print(f"Coffee: {machine_coffee}g")
    print(f"Money: ${machine_money}")
    

def input_coffee(message):
    while True:
        try:
            inpt = input(message).strip().lower()
            if inpt == 'off':
                exit() 
            elif inpt == 'report':
                show_report()
            elif inpt != 'espresso' and inpt != 'latte' and inpt != 'cappuccino':
                raise ValueError("Invalid input, Available options are ESPRESSO / LATTE / CAPPUCCINO")
        except ValueError as e:
            print(e)
        else:
            break
    return inpt

def make_coffee(recipe,coins):
    if coins >= recipe['price']:
        global machine_water,machine_milk,machine_coffee,machine_money
        try:
            machine_water -= recipe['water']
            machine_milk -=  recipe['milk']
            machine_coffee -= recipe['coffee']
            if machine_water < 0:
                raise ValueError('Sorry water is not sufficient :( ')
            if machine_milk < 0:
                raise ValueError('Sorry milk is not sufficient :( ')
            if machine_coffee < 0:
                raise ValueError('Sorry coffee is not sufficient :( ')
        except ValueError as e:
            print(e)
            machine_water += recipe['water']
            machine_milk += recipe['milk']
            machine_coffee += recipe['coffee']
        else:
            if coins > recipe['price']:
                print(f"Here is your change: {format(coins-recipe['price'],'.2f')}$")
            machine_money += recipe['price']
            print(f"Here is your {recipe['name']}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money Refunded.")
    return


def get_int(message):
    while True:
        try:
            input_integer = int(input(message))
        except ValueError:
            pass
        else:
            break
    return input_integer
        
def calculate(n_of_qtr,n_of_dms,n_of_nikl,n_of_pns):
    total_c = (n_of_qtr*0.25)+(n_of_dms*0.10)+(n_of_nikl*0.05)+(n_of_pns*0.01)
    return total_c

def accept_coins(coffee):
    quarters = get_int("Enter no. of quarters : ")
    dimes = get_int("Enter no. of dimes : ")
    nickles = get_int("Enter no. of nickles : ")
    pennies = get_int("Enter no. of pennies : ")
    total = calculate(quarters,dimes,nickles,pennies)
    return total
    
def machine():
    while True:
        coffee_input = input_coffee("\nWhat would you like? (espresso/latte/cappuccino): ")
        if coffee_input != 'report':
            coins = accept_coins(coffee_input)
            if coffee_input == 'espresso' :
                make_coffee(coffee_info[0],coins)
            elif coffee_input == 'latte':
                make_coffee(coffee_info[1],coins)
            elif coffee_input == 'cappuccino' :
                make_coffee(coffee_info[2],coins)
        print()
            
machine()