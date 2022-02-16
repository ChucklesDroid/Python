#  Importing random module to make random choices
import random

choices = ["rock", "paper", "scissors"]     #Choice for computer
computer = random.choice(choices)           #Random value alloted to computer

play_again = 1 
while play_again:
    player = None
    while player not in choices:
        print("--------Rock Paper Scissor game-------")
        player = input("Enter your choice :").lower()

    print("Computer :",computer)
    print("User :", player)

    if player == computer:
        print("Tie !!") 
    elif player == 'rock':
        if computer == 'scissor':
            print("You win !!")
        elif computer == 'paper':
            print("You lose !!")
    elif player == 'paper':
        if computer == 'rock':
            print("You win !!")
        elif computer == 'scissors':
            print("You lose !!")
    elif player == 'scissors':
        if computer == 'paper':
            print("You win !!")
        elif computer == 'rock':
            print("You lose !!")
    response = input("Do you want to play again (yes/no) ?").lower()
    play_again = 1 if response == 'yes' else 0          # Ternary operator



