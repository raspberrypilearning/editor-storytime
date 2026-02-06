<h2 class="c-project-heading--task">Challenge: Create more parts to the story</h2>

--- task ---

Have some fun with creating your story! Be as imaginative and creative as you like!

--- /task ---


--- task ---

To help you get started there are two more lists and more parts to the story below.

--- /task ---


--- task ---

Edit the code and add to the story with your own lists, and story parts.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 17-18, 23-24, 30-33, 36
---
# Possible choices 
actions = ["slay", "kiss", "chase", "marry", "rescue", "eat"]
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

# Choose randomly
action = choice(actions)
thing = choice(things)
friend = choice(friends)
place = choice(places)

# Parts of the story
start = "Once upon a time, there was a " + size + " dragon called " + name + "."
description = name + " was very " + phase + "."
hobby = " It liked to " + action + " " + thing + "."
problem = " Sadly, the dragon was so great at this that it ran out of " + thing + "."
helper = " Luckily the dragon had a friend called " + friend + " who knew where to find more " + thing + "."
journey = " They traveled far away and found lots of " + thing + " in " + place + "."
ending = " They lived happily ever after with all the " + thing + " they wanted."

# Assemble it
story = start + description + hobby + problem + helper + journey + ending
--- /code ---

--- task ---

**Test**: Run your code to create your story!

--- /task ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

- You could create a list of `enemies` or `heroes`. 
- Or give the dragon more detail with a list called `colours` that decides what colour skin the dragon's scales are
- Or a list called `breath` that determines whether the dragon breathes fire, steam, or frost.

</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging

- Make sure you follow the formatting exactly. A comma or line indent out of place will cause an error.
- Error messages sometimes have line numbers, if you get an error check the line for any mistakes.
- Make sure you add the new parts you make to `story`
- There are spaces 

</div>
