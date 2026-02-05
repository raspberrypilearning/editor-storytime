<h2 class="c-project-heading--task">Start the story</h2>

--- task ---

Use the dragon's `name` in a `story` and print to the screen.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 7-9
---
from random import choice

print("We are going to tell a story about a dragon!")

# input from user
name = input("What is the name of the dragon?")


# The story is made in parts
start = "Once upon a time, there was a dragon called " + name + "."


# Add the story parts together
story = start

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

In Python, you can use `+` to join text together.

</div>