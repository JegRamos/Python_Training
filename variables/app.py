'''
Created on 30 Jun 2018

@author: jegramos
'''

# adding variables
a = 5
b = 5

print(a + b)

# dividing numbers
# / - will always return a float 
print(a / b)

# // - for integer division
print(a // b)


# String interpolation with F-strings
guest = 8

greeting = f"The number of guest you have is {guest}"

print(greeting)

# Converting Data types
decimal = 12.355488

int_decimal = int(decimal)
str_decimal = str(decimal)

print(int_decimal + 9.0)
print(str_decimal)

# Float decimal number
number = 14.255484841
print(f"{number:1.2f}") #* Change to 2 decimal numbers

