<h2 class="c-project-heading--task">What does your dragon do?</h2>

--- task ---

Create a list based on what your dragon likes to do such as `slay` or `kiss`. These will form a part of the story.

--- /task ---

--- task ---

Start with the list below, and then add more actions you can think of using the same format.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 14-15
---
# Input from user
name = input("What is the name of the dragon?")
size = input("Is the dragon big or small? ")
age = input("How old is the dragon? ")
if int(age) > 1000:
    phase = "old"
else:
    phase = "young"

# Possible choices 
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]

# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = name + " was very " + phase + "."

--- /code ---

--- task ---

**Test**: Run your code again to check that it works. There will be no new outputs in this step.

--- /task ---

</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure you follow the same format when adding new actions.

</div>
