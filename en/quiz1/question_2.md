
--- question ---

---
legend: Question 2 of 3
---

Your Encoded Art project used parameters in functions to create customisations of shapes. The code below also uses a function with parameters. What will be the output of this code when it is run?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
food = ['fries', 'apple', 'pasta']

def find_apple(food):
    
    for item in food:
        if item == 'apple':
            print('Apple found!')
        else:
            print('Not an Apple')

find_apple(food)

--- /code ---

--- choices ---

- ( ) 
`Apple found!`
  --- feedback ---
Correct, the **list** will be **passed** to the function. The function will then check each item in the list and find the `apple` item. This will result in the message `Apple found!` being displayed. 
  --- /feedback ---

- ( ) 
There will be an error because you cannot pass a list as an **argument**.
  --- feedback ---
Not quite, you **can** pass a list as an argument so this wouldn't cause an error. 
  --- /feedback ---

- ( ) 
There will be an error because `Apple` in the print function doesn't match `apple` in the list. 
  --- feedback ---
I can see what you did there. However, if you take a look at the **list items** on **line 1** then you will see that they are all in **lowercase**. Then, take a look at the **condition** on **line 6** you will see that it is also looking for a lowercase word. This means the condition will be **true**.  
  --- /feedback ---

- (x) 
```python
Not an Apple
Apple found!
Not an Apple
```
  --- feedback ---
Almost. Those two print functions are part of a selection statement. This means that **line 7** will run if the condition is true and **line 9** will run if the condition is false. Is the condition **true** or **false**?
  --- /feedback ---

--- /choices ---

--- /question ---
