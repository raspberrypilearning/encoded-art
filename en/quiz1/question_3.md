
--- question ---

---
legend: Question 3 of 3
---

Daniel has created a function to draw a shape. This is the function that he has created:

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

He has also created a function call that is used to draw the shape in the colour that he has chosen:

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

Why does he get an error message when he runs this code?
--- /code ---

--- choices ---

- ( ) 
Colour is spelt incorrectly. 

  --- feedback ---
Good try! However, Python uses American English. `color` is the correct identifier for assigning colour values. In England, **colour** is spelt with a **u**. 
  --- /feedback ---

- ( ) 
On **line 85**, `red` should have apostrophes `''` either side. 

  --- feedback ---
Not quite. `red` is a variable so the apostrophes are not needed in this scenario. 
  --- /feedback ---

- (x) 
The function that he created has **two** parameters. This means that he needs to pass two **arguments** to the function. He only has **one** at the moment. 

  --- feedback ---

  --- /feedback ---

--- /choices ---

--- /question ---
