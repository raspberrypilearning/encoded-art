## Choose a theme

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Have you got some ideas about what sort of art you would like to make? In this step we will plan your art and set up your background.
</div>
<div>
![Image showing the different output of a prototype project when using different text](images/output_shots.png)
</div>
</div>

--- task ---

Open the [starter project](https://trinket.io/python/c4cbf837f8){:target="_blank"}. Trinket will open in another browser tab.

--- /task ---

--- task ---

**Choose:** Think about the kind of art you want to make: 
+ Do you want to choose something from your heritage or popular culture? 
+ Will your art import existing images or draw geometric shapes? 
+ What colours do you want to use?
+ Will your background be a solid colour, or made up of multiple coloured shapes?  

--- /task ---

The first thing to do when creating art using the Python `Processing library` is to add `def setup():` to define a `setup` function that is run once at the beginning of your programme.

--- task ---

**Create:** Define the `setup` function in your code to set the output window size.

--- collapse ---
---
title: Setting the screen size when your programme starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():   
    size(400, 400) #400 by 400 works well for an art canvas

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Choose:** Experiment with the numbers and run your code to find a size that you are happy with.  

--- /task ---

The `draw()` function function continuously executes the lines of code contained inside its block until the program is stopped. It is automatically called directly after `setup()`.

--- task ---

**Create:** Define the `draw` function in your script.

--- /task ---

--- task ---

**Choose:** Think about the colours you will use for your art and create some variables that will hold the colour values in `draw()`.

[[[generic-theory-simple-colours]]]

You could also use something like the [Paletton colour scheme designer](https://paletton.com/){:target="_blank"} to choose your colour palette and copy the tuples.

--- collapse ---
---
title: Storing colour values with variables
---

Colour tuples can be stored in variables by assigning them values in the format `color(x,y,z)`:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 12
line_highlights: 
---
draw():

    red = color(255,0,0)
    grn = color(0,255,0)
    blu = color(0,0,255)
    
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Create** a function that will draw a background shape using your colour palette and add a function call to your `draw()` function.

--- collapse ---

---
title: Setting the background colours when your programme starts
---

Define a new function called `draw_background()` and create a call to it in `draw():`, after a call to `no_stroke()`. If you add more parameters, this function can draw multiple shapes in different colours to create cool backgrounds:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start:11
line_highlights: 
---
def draw_background(colour):
  
    # Background colour
    fill(colour)
    rect(0, 0, 400, 400)

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 18
line_highlights: 24-25
---
def draw():

    red = color(255,0,0)
    grn = color(0,255,0)
    blu = color(0,0,255)

    no_stroke()
    draw_background(red)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Create** a call to `run()` at the very end of your script, to run the program:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 25
line_highlights: 28
---
    draw_background(red)


run()
--- /code ---

--- /task ---

--- task ---

**Test:** Run your project to see your chosen screen size and background colour. 

--- /task ---


--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: I've updated my size and colour but the output area stays the same
---

After changing the code, you will need to `run` your project to see the changes in the output area. 

Make sure you have a call to `run()` at the very end of your script outside of any of your function definitions (not indented).

--- /collapse ---

--- collapse ---

---
title: I've tried different numbers but the background colour doesn't change 
---

The maximum amount of red, green, or blue is `255`. Make sure all your `background` colour values are between `0` and `255`.  

--- /collapse ---

--- /task ---

--- save ---
