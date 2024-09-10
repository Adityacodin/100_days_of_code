import art 

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calculation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def is_valid(operator):
    operators = '+-*/'
    if not operator in operators:
        return False
    return True

def Calculator():
    to_continue = None
    result = 0
    while True:
        if to_continue == None or to_continue == 'n':
            print("\n"*20)
            print(art.logo1,art.logo2)
            first_number = int(input("First Number: "))
            result = 0
        else:
            first_number = result
        operator = input("\nPick an operation ( + - * / ): ")
        if is_valid(operator):
            second_number = int(input("Second Number: "))
            result = calculation[operator](first_number,second_number)

            print("\n",first_number,operator,second_number,"=",result,"\n")
            to_continue = input(f"Type 'y' to continue with {result} or 'n' for new calculation.")
        else:
            print("Invalid operator")

Calculator()