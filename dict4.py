def translate_shorthand(dictionary):
    for key, value in sorted(dictionary(items())):
            print(key, value)

transl = {
"omg" : "oh my gosh",
"l8r" : "later",
"ttyl" : "talk to you later",
"g9" : "good night"
}

translate_shorthand(transl)

story = """
Stacy was texting. She said lol noobs suck smh. imo wow is better.
are you going to gwcsip?
"""

story_list = story.split()

new_story_list = []
for word in story_list:
    if word in phrases.keys():
        new_story_list.append(phrases[word])
    else:
        new_story_list.append(word)
print(new_story_list)
print(" ".join(new_story_list))
