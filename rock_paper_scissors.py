# We will write a rock paper scissors game in class - Complete it in this file
import random 

# Create a function that gets the choices 
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Rock, paper, or scissors? ")
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

#function to check for a win
def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors, you win! :D"
        else:
            return "paper covers rock, you lose! :("
    elif player == "paper":
        if computer == "scissors":
            return "scissors cuts paper, you lose! :("
        else:
            return "paper covers rock, you win! :D"
    elif player == "scissors":
        if computer == "paper":
             return "scissors cuts paper, you win! :D"
        else:
            return "rock beats scissors, you lose! :("


choices = get_choices()
#print(choices)

result = check_win(choices["player"], choices["computer"])
print(result)