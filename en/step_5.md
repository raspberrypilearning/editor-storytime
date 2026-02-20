<h2 class="c-project-heading--task">How big is the dragon?</h2>

--- task ---

Ask about the dragon's `size` and `age`. **Add the size** answer to the `start` of your the story.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 7-8, 11
---
# Input from user
name = input('What is the name of the dragon?')
size = input('Is the dragon big or small?')
age = input('How old is the dragon? Type numbers only ')

# Parts of the story
start = 'Once upon a time, there was a ' + size + ' dragon called ' + name + '.'
--- /code ---

--- task ---

**Test**: Run your code again and check that the story has changed.

--- /task ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Make sure the age is in numbers or there will be an error

</div>


