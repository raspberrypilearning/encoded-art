## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---

---
legend: Question 1 of 3
---
In your Encoded art project you used lists and dictionaries to encode a shape to a letter. The code below uses **lists** and **dictionaries**. What will the be the output of this code when it is run?

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---
code = { 'a' : ['Green', 4], 'b' : ['Blue', 3], 'c' : ['Purple', 9], }

instructions = code['a']

print(instructions[0])

--- /code ---

--- choices ---

- ( ) `'Green, 4'`

  --- feedback ---

Almost, the value in the square brackets `[]` on **line 9** represents a single item from a list.

  --- /feedback ---

- ( ) `a`

  --- feedback ---

Not quite, this is the name of the **key** that has been accessed on **line 7**. Think about the data that is **paired** with the key.

  --- /feedback ---

- (x) `Green`

  --- feedback ---

Correct! A new list called `instructions` is created that will hold the items `'Green'` and `4`. The print function is then used to print the first item in that list, which is `Green`.

  --- /feedback ---

- ( ) `4`

  --- feedback ---

You are very close. The print function will display an item from the `instructions` list, but not this one.

  --- /feedback ---

--- /choices ---

--- /question ---
