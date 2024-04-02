
--- question ---

---
legend: Question 3 sur 3
---

Tu as créé une fonction pour dessiner une forme. Voici la fonction que tu as créée :

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

Tu as également créé un appel de fonction qui permet de dessiner la forme dans la couleur que tu as choisie :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 83
line_highlights:
---
red = Color(255, 0, 0)

forme_1(rouge)

--- /code ---

Pourquoi reçois-tu un message d'erreur lorsque le code s'exécute ?

--- choices ---

- ( ) La couleur est mal orthographiée.

  --- feedback ---

Bien essayé ! Cependant, Python utilise l'anglais américain, donc `color` est l'identifiant correct pour attribuer des valeurs de couleur. Dans d'autres pays anglophones, **color** s'écrit avec un **u**.

  --- /feedback ---

- ( ) À la **ligne 85**, `rouge` devrait avoir des apostrophes `''` de chaque côté.

  --- feedback ---

Pas tout à fait. `rouge` est une variable donc les apostrophes ne sont pas nécessaires dans ce cas-ci.

  --- /feedback ---

- (x) La fonction que tu as créée a **deux** paramètres. Cela signifie que tu dois transmettre deux **arguments** à la fonction. Tu n’en as qu'**un** pour le moment.

  --- feedback ---

Bien vu ! Si une fonction a **deux paramètres**, alors **deux arguments** doivent lui être transmis lors de son appel.

  --- /feedback ---

--- /choices ---

--- /question ---
