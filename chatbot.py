# --- Define your functions below! ---
def Intro():
    print("Welcome to the chatbot!")
def greeting():
    print("How are you today?")
def convers():
    print("I'm a doctor.")
    rep = input("My favorite food is burgers. I also enjoy French fries. How about you?")
    print("I'm sorry. I have lost interest in you. Goodbye.")
def is_valid_input(response, all_valid_inputs):
    valid_input = ["Hi!", "love me", "Come here often?", "I need a cheeto",]
    if response in valid_input:
        return True
    else:
        return False


    # --- Put your main program below! ---
def main():
    is_valid_input = ["Hi!", "love me", "Come here often?", "I need a cheeto", "Who's there?", ""]
    Intro()
    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer == "Hi":
                greeting()
            elif answer in ["Hi!", "love me", "Come here often?", "I need a cheeto"]:
                convers()
        else:
                print("These are the inputs I don't understand: ")
                for vi in valid_input:
                    print(vi)
                print("I don't understand anything else")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
