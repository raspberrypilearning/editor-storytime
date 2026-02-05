<h2 class="c-project-heading--task">How big is the dragon?</h2>

--- task ---

Ask about the dragon's `size` and use the input in the story.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8-12
---
from random import choice

print("We are going to tell a story about a dragon!")

# input from user
name = input("What is the name of the dragon?")
size = input("Is the dragon big or small? ")


# The story is made in parts
start = "Once upon a time, there was a " + size + "dragon called " + name + "."


# Add the story parts together
story = start

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

BULLET POINT DEBUG POINTS HERE (OPTIONAL)

</div>
