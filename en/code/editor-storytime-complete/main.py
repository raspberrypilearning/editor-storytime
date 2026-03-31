from random import choice

print("We are going to hear a story about a dragon!")

# Input from user
name = input("What is the name of the dragon? ")
print("Excellent, the dragon is called " + name)
size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")
age = input("How old is the dragon? (type a number only) ")
print("The dragon is " + age + " years old")

print("")
print("")

if int(age) > 1000:
    description = "old"
else:
    description = "young"

# Possible choices 
things = ["slay", "cakes", "chocolate", "rocks", "kittens"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

# Choose randomly
friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = name + " was very " + phase + "."
hobby = " It liked to " + action + " " + thing + "."
problem = " Sadly, the dragon was so great at this that it ran out of " + thing + "."
helper = " Luckily the dragon had a friend called " + friend + " who knew where to find more " + thing + "."
journey = " They traveled far away and found lots of " + thing + " in " + place + "."
ending = " They lived happily ever after with all the " + thing + " they wanted."

# Assemble it
story = start + description + hobby + problem + helper + journey + ending

print(story)
