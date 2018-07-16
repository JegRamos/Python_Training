'''
Created on 30 Jun 2018

@author: jegramos
'''
from builtins import int

# input age
# 18 - 20 : wear special wristband
# 21 and above : normal entry
# below 18 : too young

age = input("Dude, how old are you? ")

if age :
    age = int(age)
    if age >= 21 : 
        print("Okay, you can enter")
    elif age >= 18 :
        print("You have to wear a wristband, bro!")
    elif age >= 1 : 
        print("Scram you dam brat")    
    elif age <= 0 :
        print("Get back when you're born!")
else : 
    print("Enter your age, bro!")
    
    