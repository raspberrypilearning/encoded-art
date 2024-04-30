## Snelle quiz

Beantwoord de drie vragen. Er zijn tips om je naar het juiste antwoord te leiden.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---

---
legend: Vraag 1 van 3
---
In je Gecodeerde kunst-project heb je lijsten en dictionaries (woordenboeken) gebruikt om een vorm tot een letter te coderen. De code hieronder gebruikt **lijsten** en **dictionaries**. Wat zal de uitvoer zijn van deze code wanneer deze wordt uitgevoerd?

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

- ( ) `'Groen, 4'`

  --- feedback ---

Bijna juist, de waarde tussen vierkante haken `[]` op **regel 9** vertegenwoordigt maar één item uit een lijst.

  --- /feedback ---

- ( ) `a`

  --- feedback ---

Niet helemaal, dit is de naam van de **sleutel** die gebruikt is op **regel 7**. Denk aan de data die **gekoppeld is** aan de sleutel.

  --- /feedback ---

- (x) `Groen`

  --- feedback ---

Juist! Er wordt een nieuwe lijst gemaakt met de naam `instructies` die de items `'Groen'` en `4`bevat. De print functie wordt dan gebruikt om het eerste item af te drukken in die lijst, wat `Groen` is.

  --- /feedback ---

- ( ) `4`

  --- feedback ---

Je bent heel dichtbij. De printfunctie toont een item uit de `instructies` lijst, maar niet deze.

  --- /feedback ---

--- /choices ---

--- /question ---
