#TODO: define function rock_paper_scissors
import random

def rock_paper_scissors():

########### Starter code for Rock Paper Scissors ############

# TODO: Import the module (aka library) random

# TODO: Create a list of possible moves in rock paper scissors


    # Allow the computer to make a random selection on the move
    computer = random.choice(gestures)

    # TODO: Take in user input for rock, paper, or scissors
    # BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
    human_input = input("What do you choose?")
    gestures = ["rock", "paper", "scissors"]
    if human_input == gestures:
        print("Oops! Computer doesn't accept. Try again.")


    # Show the human player what the computer decided on
    print("Computer chooses {}".format(computer.upper()))

# Determine who wins
# TODO: when would there be a tie?
    if human_input == computer:
        print("You have a tie!")
# TODO: when does the computer win?
    if human_input < computer:
        print("You lost!")
# TODO: when does the human win?
    if human_input > computer:
        print("You win!")

rock_paper_scissors()
