#Import libraries
import json

file = open("tweets.json", "r")
data = json.load(file) #Load from file into a json object

for d in data:
    #Loop through the dictionary,(which corresponds to a single tweet)
    # for info_category, in in d.items():
    #     print(into_category, info)
    #d is our dictionary about our tweet
    # for user_mention in d["user_mentions"]:
        #Each user_mention is a dictionary
        #it corresponds
        # print(user_mention["screen_name"])
    print(d["retweet_count"])
    break
