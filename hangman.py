#Have a word/phrase
def display():
    phrase = "girls who code"

    guessed_letters = []
    game_over = False

display()

#Keep track of number of guesses

#Tell person if they get the right letter
  #then add to list
    if guess in phrase:
          print("You are right with your letter: {} ".format(guess))
    else:
          print("{} is not in the phrase! Try again".format(guess))
    guessed_letters.append(guess)
         #Tell user how many spaces and letters
    display = ""
    for letter in phrase
        if letter in guessed_letters:
            display += letters
        elif letter == " ":
            display += " "
    #letter has not been guessed yet
        else:
            display == "_ "
    print(display)

    total_underscores = 0
    for d in display:
        if d == "_":
            total_underscores += 1

while game_over == True:
#Give user option to input letter
    guess = input("Enter a letter: ")
    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letters
        elif letter == " ":
            display += " "
    #letter has not been guessed yet
        else:
            display == "_ "
    print(display)

    if total_underscores == 0:
        game_over = True
    else:
        game_over = False

    print("END OF GAME")
    #End the game if the user gets all the right letters in our word/phrase
