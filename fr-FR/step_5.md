## Créer ton dictionnaire

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Crée le dictionnaire qui codera chaque lettre de l'alphabet avec une forme. 
</div>
<div>
![Trois fruits Kawaii sont placés aléatoirement sur le canevas.](images/dictionary.PNG){:width="300px"}
</div>
</div>

--- task ---

**Définis** ton **dictionnaire** dans la fonction `draw()` . Assure-toi de lui donner un nom approprié et place le dictionnaire sous ta palette de couleurs mais au-dessus du reste du code que tu as ajouté.

--- collapse ---
---
title: Définir un dictionnaire
---
Voici un exemple de code de définition d'un dictionnaire :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
code = {

}

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Ajoute** toutes les lettres de l'alphabet comme **clés** dans le dictionnaire. Sois prudent avec la syntaxe que tu utilises. Il est très facile de manquer un deux-points `:` ou une virgule `,`.

--- collapse ---
---
title: Ajouter des clés à un dictionnaire
---
Voici un exemple de code montrant les **clés** ajoutées à un **dictionnaire** :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
code = { 'a': , 'b': , 'c': , 'd': , 'e': , 'f': , 'g': , 'h': , 'i': , 'j': , 'k': , 'l': , 'm': , 'n': , 'o': , 'p': , 'q': , 'r': , 's': , 't': , 'u': , 'v': , 'w': , 'x': , 'y': , 'z': , ' ': ,

} --- /code ---

**Note** que le jumelage de données n'a pas encore été saisi. Tu le feras dans la tâche suivante.

--- /collapse ---

--- /task ---

--- task ---

Chaque lettre de l'alphabet doit être **associée** à la forme **choisie** et à tous les arguments que tu dois transmettre à la fonction. Tu peux le faire en saisissant ces données dans une liste.

La liste devra contenir :
+ Le nom de la fonction de forme sous forme de chaîne, par exemple `'forme_1'`
+ Les valeurs des arguments dont ta fonction de forme a besoin, par exemple `100` pour la taille de la forme

--- collapse ---
---
title: Associer une liste à tes clés de dictionnaire
---

Voici un exemple d'une **liste** associée aux lettres de l'alphabet. Tu peux voir que chaque liste contient **trois** éléments : le **nom de la fonction**, la valeur de la **taille** et l'`objet` choisi à afficher.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
  code = { 'a': ['shape 3', 150, 'pink'], 'b': ['shape 3', 50, 'yellow'], 'c': ['shape 2', 75, 'astronaut'], 'd': ['shape 2', 80, 'astropi'], 'e': ['shape 1', 20, 'orange'], 'f': ['shape 2', 80, 'satellite'], 'g': ['shape 1', 10, 'purple'], 'h': ['shape 1', 300, 'green'], 'i': ['shape 1', 200, 'orange'], 'j': ['shape 2', 90, 'astropi'], 'k': ['shape 1', 12, 'purple'], 'l': ['shape 3', 43, 'pink'], 'm': ['shape 1', 93, 'orange'], 'n': ['shape 1', 64, 'green'], 'o': ['shape 3', 85, 'blue'], 'p': ['shape 2', 10, 'astropi'], 'q': ['shape 3', 45, 'blue'], 'r': ['shape 1', 70, 'purple'], 's': ['shape 1', 36, 'orange'], 't': ['shape 2', 74, 'astronaut'], 'u': ['shape 1', 58, 'grey'], 'v': ['shape 3', 78, 'yellow'], 'w': ['shape 1', 24, 'orange'], 'x': ['shape 2', 14, 'astropi'], 'y': ['shape 1', 67, 'purple'], 'z': ['shape 2', 70, 'astropi'], ' ': ['shape 3', 25, 'pink'] }

--- /code ---


--- /collapse ---

--- /task ---

--- task ---

**Débogage :** **exécute** et **teste** ton code. Il ne devrait pas y avoir de différence à ce stade. C'est l'occasion de voir si tu as des **erreurs de syntaxe** dans ton dictionnaire.

--- collapse ---
---
title: Corriger les erreurs de syntaxe
---

Si ton code comporte des erreurs de syntaxe, examine très attentivement la structure de ton dictionnaire. Il devrait y avoir :
+ Des accolades `{}` au début et à la fin du dictionnaire
+ Des apostrophes `'` entourant les clés (lettres de l'alphabet)
+ Un deux-points `:` entre la clé et la liste
+ La liste devrait avoir un crochet `[]` de chaque côté
+ Chaque élément de liste doit être séparé par une virgule `,`
+ Il devrait y avoir une virgule `,` à la fin de chaque **paire clé-valeur**

Tu peux revérifier ta syntaxe en jetant un œil à l'exemple de code dans **Associer une liste avec tes clés de dictionnaire** ci-dessus.


--- /collapse ---

--- /task ---


--- save ---
