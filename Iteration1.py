#Group 9: Shreshta Chowdhury, Renata Dos Santos, Md Saiful Islam, Md Younus Islam
#Coursework: OPS445NBB Group Project
#Game: Rock Paper Scissors - Test 1

import random #Importing random module

#Asking for user input and creating a list of options that computer can randomly choose from
uInput = input("Enter a choice (rock, paper, scissors): ") 
options = ["rock", "paper", "scissors"]
cInput = random.choice(options)

#if both play the same input, it will be a tie
if uInput == cInput:
    print(f"You both selected {uInput}. Both of you win!")

#if user inputs and computer inputs are different, check according to below
elif uInput == "rock" or uInput == "Rock":
    if cInput == "scissors":
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Rock beats scissors! You win!")
    else:
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Paper beats rock! You lose.")
elif uInput == "paper" or uInput == "Paper":
    if cInput == "rock":
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Paper beats rock! You win!")
    else:
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Scissors beat paper! You lose.")
elif uInput == "scissors" or uInput == "Scissors":
    if cInput == "paper":
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Scissors beat paper! You win!")
    else:
        print(f"\nYou chose {uInput}, computer chose {cInput}.\n")
        print("Rock beats scissors! You lose.")

#If user enters something unexpected, code will output an error
else:
    print("Wrong entry. Please try again!")