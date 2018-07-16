'''
Created on 1 Jul 2018

@author: jegramos
'''

# Generate a random integer from 1 to 10
# if the use input is equal to the generated number, he/she wins.
# give the user tips if his input is too low or too high.
# Ask if they want to play again

from random import randint
from builtins import int

user_guess = int(input("Enter your guess: "))

random_number = randint(1, 10)
 
game_over = False
while not game_over :
    if user_guess <= 10 and user_guess >= 1 :
        if user_guess == random_number : 
            print("You win!")
            play_again = input("Do you want to play again? [y/n] ").lower()
            while play_again != "y" and play_again != "n" :
                play_again = input("Invalid Choice! Do you want to play again? ").lower()
            if play_again == "n" :
                game_over = True
                print("Bye bye")
            elif play_again == "y" :             
                user_guess = int(input("Enter your guess: "))
                random_number = randint(1, 10)
        elif user_guess > random_number : 
            print("Too high!")
            user_guess = int(input("Enter your guess: "))
        elif user_guess < random_number : 
            print("Too low!")
            user_guess = int(input("Enter your guess: "))
    else :
        user_guess = int(input("Pick a number from 1 - 10 only: "))















