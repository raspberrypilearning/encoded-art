## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---

---
legend: Question 1 sur 3
---
Dans ton projet d'art codé, tu as utilisé des listes et des dictionnaires pour coder une forme en une lettre. Le code ci-dessous utilise des **listes** et des **dictionnaires**. Quel sera le résultat de ce code une fois exécuté ?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
code = {
    'a' : ['Vert', 4],
    'b' : ['Bleu', 3],
    'c' : ['Violet', 9],
}

instructions = code['a']

print(instructions[0])

--- /code ---

--- choices ---

- ( )
`'Vert, 4'`

  --- feedback ---

Presque, la valeur entre crochets `[]` à la **ligne 9** représente un seul élément d'une liste.

  --- /feedback ---

- ( )
`a`

  --- feedback ---

Pas tout à fait, c'est le nom de la **clé** à laquelle on a accédé à la **ligne 7**. Pense aux données qui sont **associées** à la clé.

  --- /feedback ---

- (x)
`Vert`

  --- feedback ---

Correct ! Une nouvelle liste appelée `instructions` est créée et contiendra les éléments `'Vert'` et `4`. La fonction print est ensuite utilisée pour imprimer le premier élément de cette liste, qui est `Vert`.

  --- /feedback ---

- ( )
`4`

  --- feedback ---

Tu es très proche. La fonction print affichera un élément de la liste des `instructions` , mais pas celui-ci.

  --- /feedback ---

--- /choices ---

--- /question ---
