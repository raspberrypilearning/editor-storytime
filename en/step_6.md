<h2 class="c-project-heading--task">Decide if the dragon is old</h2>
--- task ---

Use`if` and `else` to set the dragon's age to 'young' or 'old'. 

--- /task ---

--- task ---

Use a **more than** symbol `>` to test the user input. `if` dragons are more than 1000 years, they are old. `else` they are young. 

--- /task ---


--- task ---

Record the answer as `phase`. Then add the `phase` into the `description` part of the story.

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 9-12, 16, 19
---
# Input from user
name = input("What is the name of the dragon?")
size = input("Is the dragon big or small? ")
age = input("How old is the dragon? ")
if int(age) > 1000:
    phase = "old"
else:
    phase = "young"

# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = name + " was very " + phase + "."

# Assemble it
story = start + description

print(story) # print the story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

If you enter an age less than 1000, you should see the dragon is young.
If you enter an age more than 1000, you should see the dragon is old.

--- /task ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Check that you added `+ description` to make the story.

</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

In Python, there is a difference between the **character** '1' and the **number** `1`. Using `int(age)` makes the input into a **number**.

</div>

