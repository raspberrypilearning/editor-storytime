<h2 class="c-project-heading--task">What does your dragon do?</h2>

--- task ---

Create a list of stuff your dragon likes to do such as `slay` or `kiss`. These will form part of the story.

--- /task ---

--- task ---

Start with the list below, and then add more actions using the same format.

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

# story parts
start = "Once upon a time, there was a " + size + "dragon called " + name + "."
description = " The dragon was very " + state + "."


# Add the story parts together
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>
