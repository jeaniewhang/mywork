#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Bread", "Salad", "Roast Beef", "Cake", "Mousse", "Grilled Chicken", "Hamburger"]
#Generates a random integer.
response = input("Would you like some food?(Y/N)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
    else:
        print("{} is not a food".format(response))
    response = input("Would you like some food?(Y/N)")
