#Write a function, pretty_print_dict, that prints a given dict in sorted order
def pretty_print_dict(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

#Key is color in english, value is color in french
colors = {
"orange" : "orange",
"red" : "rouge",
"yellow" : "jaune",
"green" : "vert",
"blue" : "bleu",
"purple" : "violet"
}
pretty_print_dict(colors)

Mimi = {"height": "5 foot 4",
        "born": "Taiwan",
        "birthday": "February 26"}
