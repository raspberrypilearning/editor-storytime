<h2 class="c-project-heading--task">Start the story</h2>

--- task ---

Use the dragon's `name` in a `story` and print to the screen.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 8-14
---
# Input from user
name = input("What is the name of the dragon?")

# Parts of the story
start = "Once upon a time, there was a dragon called " + name + "."

# Assemble it
story = start

print(story) # prints story, keep this at the end
--- /code ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

In Python, you can use `+` to join text together.

</div>