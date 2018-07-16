'''
Created on 1 Jul 2018

@author: jegramos
'''

# Sino mauuna (Scrum meeting)
from random import randint

employee_list = ["Jeg", "Sarah", "Jona", "Gie", "Shirley"]

number = 1
while len(employee_list) > 0 :
    next_in_line = employee_list.pop(randint(0, len(employee_list) - 1))
    print(f"{number}. {next_in_line}")
    number += 1
