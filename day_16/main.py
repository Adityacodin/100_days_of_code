from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu,MenuItem

menu = Menu()
coffee_m = CoffeeMaker()
money_m = MoneyMachine()
while True:
    coffee_input = input(f"What coffee would you like ? ({menu.get_items()}): ").lower()
    if coffee_input == 'report':
        coffee_m.report()
        money_m.report()
    elif coffee_input == 'off':
        break
    else:
        coffee = menu.find_drink(coffee_input)
        if coffee_m.is_resource_sufficient(coffee) and money_m.make_payment(coffee.cost):
            coffee_m.make_coffee(coffee)
