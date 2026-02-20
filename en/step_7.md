<h2 class="c-project-heading--task">What does your dragon do?</h2>

--- task ---

Create a list based on what your dragon likes to do such as `slay` or `kiss`. These will form a part of the story.

--- /task ---

--- task ---

Use `choice(actions)` to pick a hobby from `actions`. Store it as `action`, and use in your story.

--- /task ---

--- task ---

Start with the list below, and then add more actions you can think of using the same format.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 11
line_highlights: 14-18, 23, 26
---
else:
    phase = 'young'

# Possible choices 
actions = ['slay', 'kiss', 'save', 'marry', 'rescue', 'eat']

# Choose randomly
action = choice(actions)

# Parts of the story
start = 'Once upon a time, there was a ' + size + ' dragon called ' + name + '.'
description = name + ' was very ' + phase + '.'
hobby = ' It liked to ' + action + '.'

# Assemble it
story = start + description + hobby
--- /code ---

--- task ---

**Test**: Run your code and check the output.
Each time you run the code, the there will be a random `choice` from the `actions` list added to the story.

--- /task ---

</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure you follow the same format when adding new actions. 
- the words you write are known as **strings** and they need to be 'inside quotes'
- each word is separated by a comma 
- the list of actions is written inside **[square brackets]**  

</div>
