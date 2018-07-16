'''
Created on 1 Jul 2018

@author: jegramos
'''
from builtins import int

# Clean up your room program

num_times = input("How many times do I have to tell you!? ")

num_times = int(num_times)

for i in range(num_times) : 
    
    print("CLEAN YOUR ROOM!")
    

# Exercise 
# Loop through 1 - 20
# 4 and 13 print x is UNLUCKY
# 7 print x is LUCKY
# for even numbers print x is EVEN
# for odd numbers print x in ODD

for number in range(1, 21) : 
    
    if number == 4 or number == 13 :
    
        print(f"{number} is UNLUCKY")
        
    elif number == 7 : 
        
        print(f"{number} is LUCKY")
    
    elif (number % 2) == 1 : 
        
        print(f"{number} is ODD")
        
    elif (number % 2) == 0 :
        
        print(f"{number} is EVEN")
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

