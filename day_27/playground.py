# unlimited positional arguments
def add(*num):
    print()
    for n in num:
        print(n)

add(1,2,3,4,5,6,7,7,7,7,5,3,)

# unlimited keyword argmuments
class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

car = Car(make = 'Nissan',model = 'GT-R')
print(car.make)
print(car.model)

