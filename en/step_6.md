<h2 class="c-project-heading--task">Decide if the dragon is old</h2>
--- task ---

Use`if` and `else` to set the dragon's age to 'young' or 'old'. 

--- /task ---

Dragons live for a long time. They are only old if their age is more than 1000 years!

--- task ---

Use **more than** (`>`) to test the user input. `if` dragons are more than 1000 years, they are old. `else` they are young.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 14-19
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

--- /code ---
--- task ---

**Test**: Run your code again and check the output.

If you enter an age less than 1000, you should see the dragon is young.

If you enter an age more than 1000, you should see the dragon is old.

--- /task ---

</div>

<div class="c-project-callout c-project-callout--tip">

In Python, there is a difference between the **character** '1' and the **number** `1`. Using `int(age)` makes the input into a **number**.

</div>

