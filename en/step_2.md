## Choose a theme

<div style="display: flex; flex-wrap: wrap;">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Have you got some ideas about what sort of art you would like to make? In this step you will plan your art and set up your background.
</div>
<div>
![Image showing the different outputs of a prototype project when using different texts as inputs.](images/output_shots.png)
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

The first thing to do when creating art using the Python `Processing library` is to add `def setup():` to define a `setup` function that is run once at the beginning of your program.

--- task ---

**Create:** Define the `setup()` function in your code to set the output window size. The `size()` function is used to state the size of the canvas. The arguments state the width and height in pixels. 

--- collapse ---
---
title: Set the screen size when your program starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: false
line_number_start: 1
line_highlights: 2-3
---
def setup():   
  size(400, 400) # 400 by 400 works well for an art canvas

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Choose:** Experiment with the numbers in your `setup()` function and run your code to find a size that you are happy with.  

--- /task ---

The `draw()` function continuously executes the lines of code contained inside its block until the program is stopped. It is automatically called directly after `setup()`.

--- task ---

**Create:** Define the `draw` function in your script.

--- /task ---

--- task ---

**Choose:** Think about the colours you will use for your art and create some variables that will hold the colour values in `draw()`.

[[[generic-theory-simple-colours]]]

You could also use something like the [Paletton colour scheme designer](https://paletton.com/){:target="_blank"} to choose your colour palette and copy the RGB values.

--- collapse ---

---
title: Colour in p5
---

The p5 color() function expects three numbers: one each for red, green, and blue.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
blue = color(50, 70, 206) #Red = 50, Green = 70, Blue = 206

--- /code ---

--- /collapse ---

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
You may notice two spellings of the word **colour** (color) in this project. The shorter one, <span style="color: #0faeb0">color</span>, is the preferred spelling in the United States. Other countries may use the longer form, <span style="color: #0faeb0">colour</span>. Any predefined code, like `color()` typically uses the American spelling.
</p>

--- task ---
**Create** a function that will **draw a background** shape using your colour palette. Next, add a call to your `draw()` function.

--- collapse ---
---
title: Set the background colours when your program starts
---

Define a new function called `draw_background()` and create a call to it in `draw():`, after a call to `no_stroke()`. 

--- code ---
---
language: python
filename: main.py - draw_background()
line_numbers: false
line_number_start: 1
line_highlights: 1-4
---
def draw_background(colour):
  # Background colour
  fill(colour)
  rect(0, 0, 400, 400)

--- /code ---

Then create a call to it in `draw()`:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 1
line_highlights: 8
---
def draw():

  red = color(255,0,0)
  green = color(0,255,0)
  blue = color(0,0,255)

  no_stroke()
  draw_background(red)

--- /code ---

If you want your background to include more colours, you will need to add more parameters.

--- code ---
---
language: python
filename: main.py - draw_background()
line_numbers: false
line_number_start: 1
line_highlights: 1, 6-7
---
def draw_background(green, blue):
  
  # Background colour
  fill(blue)
  rect(0, 0, 400, 200)
  fill(green)
  rect(0, 200, 400, 200)

--- /code ---

Then create a call to it in `draw()`:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 1
line_highlights: 7-8
---
def draw():

  red = color(255, 0, 0)
  green = color(0, 255, 0)
  blue = color(0, 0, 255)

  no_stroke()
  draw_background(green, blue)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Create** a call to `run()` at the very end of your script (with no indent!) to run the program:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
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
