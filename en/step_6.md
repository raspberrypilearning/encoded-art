## Encode a message

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Use the dictionary to encode text by placing shapes for each character in the message.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![Image showing three different randomised pictures of orange squares, grey triangles and blue circles](images/random-art.png)
</div>
</div>

--- task ---

**Remove** the test shape calls in your `draw()` function by **commenting them out** with a hashtag at the start of each line:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 
line_highlights: 
---
#shape_1(primary_2, 100)
#shape_2(primary_2, 200)
#shape_3(complementary_2, 100)

--- /code ---

--- /task ---


--- task ---

**Create** an `input()` call for the user to be able to type in their message when the program runs. We will store this input as `name`. 
This needs to go before your `run()` call, after your dictionary and outside of any function definitions.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---

name = input()

run()
--- /code ---

--- /task ---

--- task ---

Add a `print` statement before the `input()` call, to prompt the user to enter some text when the program runs:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---

print('Type some text and press Enter to generate an encoded artwork:')
name = input()

run()
--- /code ---

--- /task ---

The last thing to do is to take the user input and create a message which will be encoded using the dictionary you created.

--- task ---

At the end of your `draw()` function (after your dictionary), call the global variable `name` and convert it to lower case to avoid confusion:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 1
line_highlights: 5-7
---
' ': ['shape 1', 25, complementary_1],

}

global name

name = name.lower()

--- /code ---

--- /task ---

--- task ---

**Create** a list called `message` to hold the series of letters in the message ready to encode, then populate the list by using `append` to add the coded dictionary values for each letter:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 
line_highlights: 
---

global name

name = name.lower()

message = []

for letter in name:
    message.append(code[letter])
--- /code ---

--- /task ---

**Create** a `for` loop which will sort the `message` list of coded values based on the first term in each entry, then pass the information into your shape functions to draw a shape for each letter and place it on your canvas.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 
line_highlights: 
---
for item in message:
  if item[0] == 'shape 1':
    shape_1(item[1], item[2])
  elif item[0] == 'shape 2':
    shape_2(item[1], item[2])
  elif item[0] == 'shape 3':
    shape_3(item[1], item[2])

--- /code ---

--- collapse ---
---
title: Iterating coordinates for linear placement
---
If you are using specific coordinates to place your shapes, you will need to change the global `startx` and `starty` values inside your `for` loop and pass them back into your functions each time. 

You need the `x` coordinate of each shape to change by the `size` of the last shape, to make sure they line up nicely.

You will also need to check whether your next shape is about to be drawn outside your window by calling the `check_size()` function you created earlier (which will move the next shape to the 'next line' on your window):

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 1
line_highlights: 3-4
---
for item in message:
  if item[0] == 'shape 1':
    shape_1(item[1], item[2]) 
    startx += item[1] 
    size_check() # Check to see if you've gone off the side of the window
  elif item[0] == 'shape 2':
    shape_2(item[1], item[2])
    startx += item[1]
    size_check()
  elif item[0] == 'shape 3':
    shape_3(item[1], item[2])
    startx += item[1]
    size_check()

--- /code ---


--- /collapse ---
--- save ---
