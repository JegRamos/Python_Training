'''
Created on 30 Jun 2018

@author: jegramos
'''

# Conditional Statements
# if, elif, else

name = "Jeg Ramos"

if name == "Jeg Ramos":
    print(f"{name} is awesome!")
elif name == "Sarah Opena":
    print(f"Oh no it's {name}! Patatas alert!")
elif name == "Jona":
    print(f"{name} is a cool dude.")
else:
    print("What are you talking about?")

# find out if a number is odd or even
from random import randint # import randint function from random libs
random_number = randint(1, 1000) # generate a random integer from 1 - 1000

if (random_number % 2) == 0 :
    print(f"{random_number} is even")
elif (random_number % 2) == 1 :
    print(f"{random_number} is odd")
else:
    print("What the f did you just typed?")


