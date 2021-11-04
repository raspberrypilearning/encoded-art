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

**Define** each shape function in preparation for adding in the code that will be needed to draw each shape. 

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

**Add** your chosen **parameters** inside the curved brackets of each of your **shape** functions.

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

--- task ---

**Add** in the code for each of your shape functions so that the drawing or image will appear when the function is **called**.

--- collapse ---
---
title: Drawing your shape
---

In the [make a face project](https://projects.raspberrypi.org/en/projects/make-a-face/0){:target="_blank"} you learnt how to use a group of geometric shapes to create some fun faces. You can use your skills from that project to help you draw your images. 

Here is some sample code for drawing a square:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
def shape_2(colour, size):

  fill(colour)   
  rect(200, 200, size, size)

--- /code ---

**Notice** that the parameters that are defined in the function above are then used to draw the shape. 

--- /collapse ---

--- collapse ---
---
title: Loading images
---

The [Lost in Space](https://trinket.io/python/ff931d5dd5){:target="_blank"} example project loads images to create the encoded artwork. 

**Remember** that you will need code to display the image:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4
---def shape_1(size, colour): 
  
  if colour == 'purple':
    image(purple_planet, 400, 400, size, size)

--- /code ---

You will also need code to **load** the image in the `setup()` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10 
---
def setup():
  
  # Allow other functions to access the images
  global purple_planet
  
  frame_rate(10)
  size(400, 400)
  
  # Load the images needed into variables
  purple_planet = load_image('purple_planet.png')

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

In order to **test** that your shape functions work correctly you will need to **call** them from the `draw()` function. 

Make sure that you add in the values for your chosen parameters!

Here is an example of what your function calls might look like:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
  shape_1(primary_2, 100)
  shape_2(primary_2, 100)
  shape_3(complementary_2, 100)

--- /code ---

**Notice** that the variable names for the chosen `colour` have been placed in the first parameter and some values have been added for the chosen `size` in the second parameter. 

--- /task ---

--- task ---

**Test** your code to see if it displays your chosen images on the screen. At this point they might all appear on top of each other. You could **call** each function separately to see them more clearly. 

![A screenshot of the output of the example project. There is a dark blue background, a blue square, a blue circle and an orange triangle.](images/shape-functions.PNG)

--- /task ---

--- task ---

**Debug:** 

--- collapse ---
---
title: You see an error about arguments
---
+ When you **defined** your function you decided how many **parameters** it needed. You need to make sure that when you call the function, it has the same number of **arguments**.

--- /collapse ---

--- collapse ---
---
title: Only one shape appears
---
+ Check that you have **called** each shape function
+ The shapes might be there, but on top of each other. To change this you could call one function at a time by commented out the other two function calls with a hashtag `#`

--- /collapse ---

--- collapse ---
---
title: The drawings are not the right shape/size
---
+ Check that you have entered your parameters the right way round. 

--- /collapse ---

--- /task ---


--- save ---
