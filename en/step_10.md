<h2 class="c-project-heading--task">Challenge: Create more parts to the story</h2>

--- task ---

Have some fun with creating your story! Be as imaginative and creative as you like!

--- /task ---


--- task ---

Below there are two more lists and more parts to the story to help you get started.
- the names of the dragon's `friends`
- a list of `places` such as "Middle Earth" and "Narnia"

--- /task ---


--- task ---

Add to the story with your own lists, and story parts.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 19
line_highlights: 22-24
---

from random import choice

print("We are going to tell a story about a dragon!")

# input from user
name = input("What is the name of the dragon?")
size = input("Is the dragon big or small? ")
age = input("How old is the dragon? ")
if int(age) > 1000:
    phase = "an old"
else:
    phase = "a young"

# possible choices for the story 
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]


# story parts
start = "Once upon a time, there was a " + size + "dragon called " + name + "."
description = " The dragon was very " + state + "."
hobby = " It liked to " + choice(actions) + " " + choice(things) + "."
problem = " Sadly, the dragon was so great at this that it ran out of " + choice(things) + "."
helper = " Luckily the dragon had a friend called " + choice(friends) + " who knew where to find more " + choice(things) + "."
journey = " They travelled far away and found lots of " + choice(things) + " in " + choice(places) + "."
ending = " They lived happily ever after with all the " + choice(things) + " they wanted."


# Add the story parts together
story = start + description + hobby + problem + helper + journey + ending

print(story) # prints story, keep this at the end

print("It was an " + description + " dragon.")


--- /code ---

--- task ---

**Test**: Run your code to create your story!

--- /task ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

- You could create a list of `enemies` or `heroes`. 
- Or give the dragon more detail with a list called `colours` that decides what colour skin the dragon's scales are
- Or a list called `breath` that determines whether the dragon breathes fire, steam, or frost.

</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging

- Make sure you follow the formatting exactly. A comma or line indent out of place will cause an error.
- Error messages sometimes have line numbers, if you get an error check the line for any mistakes.
- Make sure you add the new parts you make to `story`
- There are spaces 

</div>
