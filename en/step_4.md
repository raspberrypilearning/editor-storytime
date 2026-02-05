<h2 class="c-project-heading--task">Start the story</h2>

--- task ---

Use the `name` variable to print the name to the screen. 

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

print("We are going to tell a story about a dragon!")

name = input("What is the name of the dragon? ")

story = "Once upon a time, there was a dragon called " + name" 

print(story)

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

In Python, you can use `+` to join text together.

</div>