<h2 class="c-project-heading--task">Add more things</h2>

--- task ---

Add to the hobby part by creating a list of more things your dragon likes such as `goblins` or `cakes`.

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 21
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

# story parts
start = "Once upon a time, there was a " + size + "dragon called " + name + "."
description = " The dragon was very " + state + "."
hobby = " It liked to " + action + " " + thing + "."


# Add the story parts together
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>
