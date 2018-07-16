'''
Created on 1 Jul 2018

@author: jegramos
'''

# Mimic game
your_statement = input("Hey how's it going? ")

while your_statement != "stop copying me" : 
    sister_statement = your_statement
    print(sister_statement)
    your_statement = input()
print("UGH FINE, YOU WIN")