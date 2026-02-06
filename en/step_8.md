<h2 class="c-project-heading--task">Choose random details</h2>

--- task ---

Use `choice()` to pick one of the words from `actions` at random, this makes the story different each time.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 26-27
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

# story parts
start = "Once upon a time, there was a " + size + "dragon called " + name + "."
description = " The dragon was very " + state + "."
hobby = " It liked to " + choice(actions) + "."

# Add the story parts together
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---
</div>
--- task ---

**Test**: Run your code and check the output.
Each time you run the code, the there will be a random `choice` from the `actions` list added to the story.
--- /task ---

