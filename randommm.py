#TODO: import the random module since you  will need it in your game functions
import random

#TODO: define function guess_the_num
def guess_the_num(number):

#TODO: use random.randint to get a number between 1 and 20
    number = random.randomint(1,20)
    #TODO: ask user to input their guess
    response = input("What number do you guess?")
        #TODO: loop to keep giving the player three guesses until they've guessed correctly
    tries = 0
    while tries == 3:
        tries += 1
        if response >= number:
            print("Guess lower")
        elif response <= number:
            print("Guess higher")
        else:
            print("You've got it!")
    print(tries)
        #TODO: give the player cues if the guess is not correct
#already did; test it out
    #TODO: let the player know if the guess is correct
#already did; test it
