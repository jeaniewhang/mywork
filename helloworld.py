"""
Challenge 1: Create a Guess the Number game using a for loop
and limit the player to three tries/
Tell them if they should guess higher or lower next time.
"""
number = 15
tries = 0

guess = int(input("What number is it?"))
for tries in range(3):
    tries += 1
if int(input("What number is it")) < number:
    print("Guess higher")
elif int(input("What number is it")):
    print("Guess lower"):
else:
    print("The number is {}".format(number)):

answer = "umbrella"
tries = 0
guess = input("What goes up when the rain comes down?")
for tries in range(2):
    tries += 1
    if guess != answer
        guess= input("Try again! Hint: What do you use when it rains?")
print("The answer is an {}".format(answer))
