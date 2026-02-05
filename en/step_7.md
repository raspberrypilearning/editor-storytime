<h2 class="c-project-heading--task">Add other things to your story</h2>

--- task ---

Create a list of different things such as `goblins` or `cakes` that the dragon can interact with. 

--- /task ---

--- task ---

The programme will pick one of the list of words at random, this makes the story different each time.

Start with the list here, and then add your own items.

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

print("We are going to hear a story about a dragon!")

name = input("What is the name of the dragon? ")
print("Excellent. The dragon is called " + name)

size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")

age = input("How old is the dragon? ")
print("The dragon is " + age + " years old")

if int(age) > 1000:
    description = "an old"
else:
    description = "a young"

print("It was an " + description + " dragon.")

things = ["goblins", "cakes", "chocolate", "rocks", "trees"]

story
--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Lists can be named in the same way as variables. For example, to create a list called `numbers` with four items in it, you could use the line `numbers = ["zero", "one", "two", "three"]`.

</div>