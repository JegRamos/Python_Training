'''
Created on 1 Jul 2018

@author: jegramos
'''

# Player VS Computer
from random import randint

player_choice = input("Enter your move: ").lower()
computer_array_choices = ["rock", "paper", "scissors"]
computer_choice = computer_array_choices[randint(0, 2)] # Choose a random integer between 1 and 3

print(f"The computer played {computer_choice}")

if player_choice == computer_choice :
    print("It's a tie")
elif player_choice == "rock" :
    if computer_choice == "scissors" :
        print("You Win!")
    elif computer_choice == "paper" :
        print("You Lose!")
elif player_choice == "paper" :
    if computer_choice == "rock" :
        print("You Win!")
    elif computer_choice == "scissors" :
        print("You Lose!")
elif player_choice == "scissors" :
    if computer_choice == "paper" :
        print("You Win!")
    elif computer_choice == "rock" :
        print("You Lose!")
else :
    print("You made an invalid input!")