## Add some random details

Your program will generate a lot of the story at random. 

You need to create some lists to store different and funny words that the program can choose from.

Lists can be named in the same way as variables. For example, to create a list called `numbers` with four items in it, you could use the line `numbers = ["zero", "one", "two", "three"]`.

--- task ---

Create a list of things that the dragon can interact with. 

Use the list of items we use here, or add your own items!

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

--- /code ---

--- /task ---
