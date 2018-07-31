def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Even or odd?")
    if (computer_value % 2 == 0)) and (user_input == "even"):
        print("You did it! You're so smort\n")
    elif((computer_value % 2) == 0) and (user_input == "odd"):
        print("You're wrong\n")
    elif((computer_value % 2) != 0) and (user_input == "even"):
        print("You're wrong\n")
    else((computer_value % 2) != 0) and (user_input == "odd")
        print("You're right!")
evenorodd()
