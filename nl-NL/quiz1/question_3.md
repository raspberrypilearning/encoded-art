
--- question ---

---
legend: Vraag 3 van 3
---

Je hebt een functie gemaakt om een vorm te tekenen. Dit is de functie die je hebt gemaakt:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
def shape_1(colour, size):

    x = randint(0, 400)
    y = randint(0, 400)
    fill(colour)   
    ellipse(x, y, size, size)
--- /code ---

Je hebt ook een functieaanroep gemaakt die wordt gebruikt om de vorm te tekenen in de kleur die je hebt gekozen:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 83
line_highlights:
---
red = Color(255, 0, 0)

vorm_1(rood)

--- /code ---

Waarom krijg je een foutmelding als de code wordt uitgevoerd?

--- choices ---

- ( ) Color is verkeerd gespeld.

  --- feedback ---

Goed geprobeerd! Python gebruikt echter Amerikaans-Engels, dus `Color` is de juiste identificatie voor het toewijzen van kleurwaarden. In andere Engelssprekende landen wordt **Colour** gespeld met een **u**.

  --- /feedback ---

- ( ) Op **regel 85** moet `rood` aanhalingstekens `''` aan weerszijden hebben.

  --- feedback ---

Niet helemaal. `rood` is een variabele, dus de aanhalingstekens zijn in dit scenario niet nodig.

  --- /feedback ---

- (x) De functie die je hebt gemaakt bevat **twee** parameters. Dit betekent dat je twee **argumenten** aan de functie moet doorgeven. Je hebt er slechts **één** op dit moment.

  --- feedback ---

Goed gezien! Als een functie **twee parameters**heeft, dan moeten **twee argumenten** eraan worden doorgegeven wanneer deze wordt aangeroepen.

  --- /feedback ---

--- /choices ---

--- /question ---
