def display(word, already_guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter

        elif letter == " ":
            new_str += " "
        else:
            new_str += "_ "
    print(new_str)
    return new_str

def main():
    phrase = "turtles are cool"

    guessed_letters = []
    game_over = False

first = display(phrase, guessed_letters)
print(first)

while game_over != True:
    guess = input("Enter a letter")
    if guess in phrase:
        print("You got a letter: {}".format(guess))

    else:
        print("{} is not in the phrase".format(guess))
    guessed_letters.append(guess)
    display(phrase, guessed_letters)

    if "_" in display:
        game_over = False
    else:
        game_over = True
    print("END OF GAME")

if __name__ == "main":
    
