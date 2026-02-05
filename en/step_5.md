<h2 class="c-project-heading--task">Size and age of the dragon</h2>

--- task ---

Ask about the dragon's `size` and `age`.

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

name = input("What is the name of the dragon? ")
print("Excellent. The dragon is called " + name)

size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")

age = input("How old is the dragon? ")
print("The dragon is " + age + " years old")

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>