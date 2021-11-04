## Draw your shapes

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Set up your shape functions so that you can use them in your encoded artwork. 
</div>
<div>
![A screenshot of the output of the example project. There is a dark blue background, a blue square, a blue circle and an orange triangle.](images/shape-functions.PNG){:width="300px"}
</div>
</div>

--- task ---

Decide how many unique **shapes** you would like your artwork to have. The example projects have **three** unique shapes. These are then modified using the parameters of the function. You might like to have more than three, the decision is yours!

Here are some ideas:
+ Three shape functions that load images of either butterflies, snails or birds. 
+ Three shape functions that draw squares, circles and triangles
+ Five shape functions, each one draws a unique animal

--- /task ---

--- task ---

Define each shape function in preparation for adding in the code that will be needed to draw each shape. 

--- collapse ---
---
title: Defining a function
---
You can define your functions in the following way:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
def shape_1():
   
def shape_2():

def shape_3():

--- /code ---


--- /collapse ---

--- /task ---

--- task ---

Decide which **parameters** your functions will need. Here are some ideas:
+ A `colour` parameter to allow you to modify the colour of the shapes that you have created
+ A `size` parameter to allow you to adjust the size of the shape or image 
+ An `outline` parameter that adds a different colour to the edge of a drawing

--- /task ---

--- task ---

Add your chosen **parameters** inside the curved brackets of each of your **shape** functions.

--- collapse ---
---
title: Adding parameters to functions
---
You can add parameters to your functions in the following way:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
def shape_1(size, colour):
   
def shape_2(size, colour):

def shape_3(size, colour):

--- /code ---


--- /collapse ---

--- /task ---



--- save ---
