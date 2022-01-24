
--- question ---

---
legend: Question 3 of 3
---

You have created a function to draw a shape. This is the function that you have created:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
def shape_1(colour, size):
  
  x = randint(0, 400)
  y = randint(0, 400)
  fill(colour)   
  ellipse(x, y, size, size)
--- /code ---

You have also created a function call that is used to draw the shape in the colour that you have chosen:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 83
line_highlights: 
---
red = color(255, 0, 0)

shape_1(red)
--- /code ---

Why do you get an error message when the code runs?

--- choices ---

- ( ) 
Colour is spelt incorrectly. 

  --- feedback ---
Good try! However, Python uses American English, so `color` is the correct identifier for assigning colour values. In other English speaking countries, **colour** is spelt with a **u**. 
  --- /feedback ---

- ( ) 
On **line 85**, `red` should have apostrophes `''` either side. 

  --- feedback ---
Not quite. `red` is a variable so the apostrophes are not needed in this scenario. 
  --- /feedback ---

- (x) 
The function that you created has **two** parameters. This means that you need to pass two **arguments** to the function. You only have **one** at the moment. 

  --- feedback ---
Well spotted! If a function has **two parameters**, then **two arguments** must be passed into it when it is called. 
  --- /feedback ---

--- /choices ---

--- /question ---
