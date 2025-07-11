## Bouw je dictionary

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maak de dictionary die elke letter van het alfabet met een vorm codeert. 
</div>
<div>
![Drie Kawaii-vruchten worden willekeurig op het canvas geplaatst.](images/dictionary.PNG){:width="300px"}
</div>
</div>

--- task ---

**Definieer** je **dictionary** in de functie `draw()`. Zorg ervoor dat je het een passende naam geeft en plaats je dictionary onder je kleurenpalet maar boven de rest van de code die je hebt toegevoegd.

--- collapse ---
---
title: Definieer een dictionary
---
Hier is wat voorbeeldcode van een ditionary die wordt gedefinieerd:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
code = {
    
}

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Voeg** alle letters van het alfabet toe als **sleutels** in het woordenboek. Wees voorzichtig met de syntax die je gebruikt. Het is heel gemakkelijk om een dubbele punt `:` of een komma `,` over het hoofd te zien.

--- collapse ---
---
title: Sleutels toevoegen aan een dictionary
---
Hier is wat voorbeeldcode die **sleutels** laat zien die worden toegevoegd aan een **dictionary**:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
code = {
    'a': ,
    'b': ,
    'c': ,
    'd': ,
    'e': ,
    'f': ,
    'g': ,
    'h': ,
    'i': ,
    'j': ,
    'k': ,
    'l': ,
    'm': ,
    'n': ,
    'o': ,
    'p': ,
    'q': ,
    'r': ,
    's': ,
    't': ,
    'u': ,
    'v': ,
    'w': ,
    'x': ,
    'y': ,
    'z': ,
    ' ': ,
    
}
--- /code ---

**Merk op** dat de datakoppeling nog niet is ingevoerd. Dit doe je in de volgende opdracht.

--- /collapse ---

--- /task ---

--- task ---

Elke letter van het alfabet moet **gecombineerd worden** met de door jou gekozen **vorm** en eventuele argumenten die je nodig hebt om in de functie door te geven. Dit kun je doen door deze gegevens in een lijst in te voeren.

De lijst moet het volgende bevatten:
+ De naam van de vormfunctie als string, bijvoorbeeld `'vorm_1'`
+ De waarden van de argumenten die jouw vormfunctie nodig heeft, bijvoorbeeld `100` voor de grootte van de vorm

--- collapse ---
---
title: Koppel een lijst met je dictionary sleutels
---

Hier is een voorbeeld van een **lijst** die wordt gecombineerd met de letters van het alfabet. Je kunt zien dat elke lijst **drie** items bevat: de **functienaam**, de **grootte** waarde en het gekozen `object` om weer te geven.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
  code = {
    'a': ['vorm 3', 150, 'roze'],
    'b': ['vorm 3', 50, 'geel'],
    'c': ['vorm 2', 75, 'astronaut'],
    'd': ['vorm 2', 80, 'astropi'],
    'e': ['vorm 1', 20, 'oranje'],
    'f': ['vorm 2', 80, 'satelliet'],
    'g': ['vorm 1', 10, 'paars'],
    'h': ['vorm 1', 300, 'groen'],
    'i': ['vorm 1', 200, 'oranje'],
    'j': ['vorm 2', 90, 'astropi'],
    'k': ['vorm 1', 12, 'paars'],
    'l': ['vorm 3', 43, 'roze'],
    'm': ['vorm 1', 93, 'oranje'],
    'n': ['vorm 1', 64, 'groen'],
    'o': ['vorm 3', 85, 'blauw'],
    'p': ['vorm 2', 10, 'astropi'],
    'q': ['vorm 3', 45, 'blauw'],
    'r': ['vorm 1', 70, 'paars'],
    's': ['vorm 1', 36, 'oranje'],
    't': ['vorm 2', 74, 'astronaut'],
    'u': ['vorm 1', 58, 'grijs'],
    'v': ['vorm 3', 78, 'geel'],
    'w': ['vorm 1', 24, 'oranje'],
    'x': ['vorm 2', 14, 'astropi'],
    'y': ['vorm 1', 67, 'paars'],
    'z': ['vorm 2', 70, 'astropi'],
    ' ': ['vorm 3', 25, 'roze']
}

--- /code ---


--- /collapse ---

--- /task ---

--- task ---

**Debug:** **Run** en **Test** je code. In dit stadium zou het niet anders moeten zijn. Dit is een kans om te zien of je **syntaxfouten** in je dictionary hebt.

--- collapse ---
---
title: Syntaxfouten herstellen
---

Als je code syntaxfouten heeft, kijk dan heel goed naar de structuur van je dictionary. Er zou moeten zijn:
+ Accolades `{}` aan het begin en einde van de dictionary
+ Aanhalingstekens `'` om de sleutels (letters van het alfabet)
+ Een dubbele punt `:` tussen de sleutel en de lijst
+ De lijst moet aan elke kant een vierkante haak `[]` hebben
+ Elk lijstitem moet worden gescheiden door een komma `,`
+ Er moet een komma `,` staan aan het einde van elk **sleutel-waardepaar**

Je kunt je syntax nog eens controleren door naar de voorbeeldcode te kijken in **Koppel een lijst met je dictionary sleutels** hierboven.


--- /collapse ---

--- /task ---


--- save ---
