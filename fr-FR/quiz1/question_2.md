
--- question ---

---
legend: Question 2 sur 3
---

Ton projet d'art codé a utilisé des paramètres dans des fonctions pour créer des personnalisations de formes. Le code ci-dessous utilise également une fonction avec des paramètres. Quel sera le résultat de ce code une fois exécuté ?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
nourriture = ['frites', 'pomme', 'pates']

def trouver_pomme(nourriture):

    for element in nourriture:
        if element == 'pomme':
            print('Pomme trouvée !')
        else:
            print('Pas une pomme')

trouver_pomme(nourriture)

--- /code ---

--- choices ---

- ( )
`Pomme trouvée !`

  --- feedback ---

Presque. Ces deux fonctions print font partie d'une instruction de sélection. Cela signifie que la **ligne 7** s'exécutera si la condition est vraie et la **ligne 9** s'exécutera si la condition est fausse. La condition est-elle **vraie** ou **fausse** ?

  --- /feedback ---

- ( )
Il y aura une erreur car tu ne peux pas transmettre une liste comme un **argument**.

  --- feedback ---

Pas tout à fait, tu **peux** transmettre une liste comme argument afin que cela ne provoque pas d'erreur.

  --- /feedback ---

- ( )
Il y aura une erreur car `Pomme` dans la fonction print ne correspond pas à `pomme` dans la liste.

  --- feedback ---

Je peux voir ce que tu as fait là. Cependant, si tu jettes un œil aux **éléments de la liste** à la **ligne 1** alors tu verras qu'ils sont tous en **minuscules**. Ensuite, jette un œil à la **condition** à la **ligne 6** et tu verras qu'elle recherche également un mot minuscule. Cela signifie que la condition sera **vraie**.

  --- /feedback ---

- (x)
```python
Pas une pomme
Pomme trouvée !
Pas une pomme
```

  --- feedback ---

Correct, la **liste** sera **transmise** à la fonction. La fonction vérifiera ensuite chaque élément de la liste et trouvera l'élément `pomme` . Le message `Pomme trouvée !` s'affichera lors du deuxième passage dans la boucle.

  --- /feedback ---

--- /choices ---

--- /question ---
