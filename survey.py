cont = True

survey = {
'name': "Please enter your name? ",
'age': "How old are you? ",
'hobbies': "What are your hobbies? ",
'animal': "What's your favorite animal? ",
'feelings': "How are you feeling? ",
'why': "Why are you here today? ",
'chips': "What's your favorite brand of chips? "
}

storage = []
while cont:
    reply = {}
    for category, surve in survey.items():
        reply[category] = input(surve)
    storage.append(reply)
    to_cont = input("Would you like to continue: yes or no ")
    if to_cont == "yes":
        cont = True
    else:
        cont = False


print(storage)
# def answers(survey):
#     for key, value in survey.items():
#         print(key, value)
#
# answers(reply)

print("Thank you for taking this survey! Your data is much appreciated. To play again, press the up button and enter.")


import json
file = open("data.json", "w")


data = [{reply()}]
f = open("data.json", "w")
#Turn data(list of dictionaries) into a json object
js_obj = json.dumps(data)

#Write the json object to our file
f.write(json_obj)

#Close our file
f.close()

#What to do when you have data but you already have a data.json file
data2 = [{reply()}]
f = open("data.json")
old_data = json.loads(f) # return a list of data that was already in data.json
old_data.extend(data2) #combine old data with new data
f.write(json.dumps(old_data))
f.close()
f2.close()
