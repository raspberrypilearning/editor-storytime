<h2 class="c-project-heading--task">Add a list of things</h2>

--- task ---

Add to the dragon's hobby by creating a list of more things your dragon likes such as `goblins` or `cakes`.

--- /task ---

--- task ---
Use `choice()` again to add a random thing to your story. 

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 17, 23
---
# Possible choices 
actions = ["slay", "kiss", "chase", "marry", "rescue", "eat"]
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]


# Choose randomly
action = choice(actions)
thing = choice(things)


# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = " The dragon was very " + state + "."
hobby = " It liked to " + action + " " + thing + "."


# Assemble it
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

</div>



