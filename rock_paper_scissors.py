# We will write a rock paper scissors game in class - Complete it in this file
import random 


# Create a function that gets the choices 
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Rock, paper, or scissors? ")
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices = get_choices()
print(choices)

