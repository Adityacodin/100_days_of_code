import random

#generates floating point numbers greater than 0 and less than 1 
random_but_0_to_1 = random.random() 
print(random_but_0_to_1)

#generates random integers betweeen the specified range all inclusive
random_integer = random.randint(1,100)
print(random_integer)

#generates random float betweeen the specified range all inclusive
random_float = random.uniform(1,11)
print(random_float)


# BILL ROULETTE
friends = ['Jay','Aditya','Anuj','Sahil']

pick = random.randint(0,len(friends)-1)
print(friends[pick])

# OR
print(random.choice(friends))