<h2 class="c-project-heading--task">Choose a random hobby</h2>

--- task ---

Use `choice(actions)` to pick a hobby from `actions`. Store it as `action`, and use in your story.

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 17-18, 23, 26
---
# Possible choices 
actions = ["slay", "kiss", "chase", "marry", "rescue", "eat"]

# Choose randomly
action = choice(actions)

# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = name + " was very " + phase + "."
hobby = " It liked to " + action + "."

# Assemble it
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---

--- task ---

**Test**: Run your code and check the output.
Each time you run the code, the there will be a random `choice` from the `actions` list added to the story.

--- /task ---

</div>