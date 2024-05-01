
--- question ---

---
legend: Vraag 2 van 3
---

Je Gecodeerde kunst-project gebruikt parameters in functies om verschilende, aangepaste vormen te maken. De onderstaande code gebruikt ook een functie met parameters. Wat zal de uitvoer zijn van deze code wanneer deze wordt uitgevoerd?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
voedsel = ['frieten', 'appel', 'pasta']

def vind_appel(voedsel):
    
    for item in voedsel:
        if item == 'appel':
            print('Appel gevonden!')
        else:
            print('Geen appel')

vind_appel(voedsel)

--- /code ---

--- choices ---

- ( )
`Appel gevonden!`

  --- feedback ---

Bijna. Deze twee printfuncties maken deel uit van een selectiestatement. Dit betekent dat **regel 7** wordt uitgevoerd als de voorwaarde waar is en **regel 9** wordt uitgevoerd als de voorwaarde onwaar is. Is de voorwaarde **waar** of **onwaar**?

  --- /feedback ---

- ( )
Er zal een fout optreden omdat je een lijst niet kunt doorgeven als een **argument**.

  --- feedback ---

Niet helemaal, je **kunt** een lijst als argument gebruiken zonder dat dit een fout veroorzaakt.

  --- /feedback ---

- ( )
Er zal een fout optreden omdat `Appel` in de afdrukfunctie niet overeenkomt met `appel` in de lijst.

  --- feedback ---

Ik begrijp wat je daar hebt gedaan. Als je echter naar de **lijstitems** op **regel 1** kijkt, zul je zien dat ze allemaal in **kleine letters staan**. Kijk dan eens naar de **voorwaarde** op **regel 6** en je zult zien dat er ook naar een woord in kleine letters wordt gezocht. Dit betekent dat de voorwaarde **waar** zal zijn.

  --- /feedback ---

- (x)
```python
Geen appel
Appel gevonden!
Geen appel
```

  --- feedback ---

Correct, de **lijst** wordt **doorgegeven** aan de functie. De functie controleert vervolgens elk item in de lijst en vindt het `appel` item. Dit resulteert in het bericht `Appel gevonden!` dat wordt weergegeven als de lus de tweede keer wordt doorlopen.

  --- /feedback ---

--- /choices ---

--- /question ---
