<h2 class="c-project-heading--task">Choose a random hobby</h2>

--- task ---

Use `choice()` to pick a hobby from `actions` at random.

--- /task ---

--- task ---

Adding `choice(actions)` to part of your story will choose a word from the `action` list at random.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 18, 22
---
# possible choices for the story 
actions = ["slay", "kiss", "chase", "marry", "rescue", "eat"]


# Choose randomly
action = choice(actions)


# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = " The dragon was very " + state + "."
hobby = " It liked to " + action + "."


# Assemble it
story = start + description + hobby

print(story) # prints story, keep this at the end

--- /code ---
</div>
--- task ---

**Test**: Run your code and check the output.
Each time you run the code, the there will be a random `choice` from the `actions` list added to the story.
--- /task ---

