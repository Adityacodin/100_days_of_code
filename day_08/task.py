# task 1
def greet():
    print("Hello Human")
    print("How are you?")
    print("Hope you are doing fine...")

greet()
print()

#task 2
# name here is said to be a PARAMETER
def greet_with_name(name):
    print(f"Hello {name}")
    print("How are you?")
    print("Hope you are doing fine...")

# "Aditya" here is what we call an ARGUMENT
greet_with_name("Aditya")
print()

# task 3
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How's the weather in {location}")

greet_with("Kiran","Mumbai")
print()

greet_with("Mumbai","Kiran") #logical error
print()
# positional arguments
greet_with(location = "Mumbai",name = "Kiran")