#!/bin/python3

# PROTOTYPE VIER

from p5 import *


def grootte_controle(): # Controleer of je buiten de zijkant van het venster bent gegaan

    global startx
    global starty
    if startx >= 400:
        startx = 0
        starty += 80


def vorm_1(grootte, kleur): # Teken een diamant

    global startx
    global starty
    x1 = startx
    y1 = starty + 40 # Ga naar het midden van de streep
    x2 = x1 + (grootte/2)
    y2 = y1 + (grootte/2)
    x3 = x1 + grootte
    y3 = y1
    x4 = x1 + (grootte/2)
    y4 = y1 - (grootte/2)
    fill(kleur)
    quad(x1, y1, x2, y2, x3, y3, x4, y4)


def vorm_2(grootte, kleur): # Teken een vierkant

    global startx
    global starty
    x = startx
    y = starty
    fill(kleur)
    rect(x, y, grootte, grootte)


def vorm_3(grootte, kleur): # Teken een driehoek

    global startx
    global starty
    x1 = startx
    y1 = starty
    x2 = x1 + (grootte/2)
    y2 = y1 + grootte
    x3 = x1 + grootte
    y3 = y1
    fill(kleur)
    triangle(x1, y1, x2, y2, x3, y3)


# Voegt een achtergrondkleur toe
def teken_achtergrond():

    # Achtergrondkleuren
    fill(Color(0, 0, 255))
    rect(0, 0, 400, 80)
    fill(Color(0, 127, 127))
    rect(0, 80, 400, 80)
    fill(Color(0, 255, 0))
    rect(0, 160, 400, 80)
    fill(Color(127, 127, 0))
    rect(0, 240, 400, 80)
    fill(Color(255, 0, 0))
    rect(0, 320, 400, 80)


def setup():

    size(400, 400)


def draw():

    # -- Mijn kleurenpalet --

    # Primaire kleuren

    primair_1 = Color(246, 32, 100)
    primair_2 = Color(247, 0, 79)
    primair_3 = Color(234, 0, 75)
    primair_4 = Color(196, 0, 63)
    primair_5 = Color(4, 0, 1)

    # Secundaire kleuren

    secundair_1 = Color(255, 198, 33)
    secundair_2 = Color(255, 190, 0)
    secundair_3 = Color(55, 190, 0)

    # Complementaire kleuren

    complementair_1 = Color(59, 63, 230)
    complementair_2 = Color(5, 9, 154)
    complementair_3 = Color(133, 246, 32)

    code = {
        'a': ['vorm 1', 80, primair_1],
        'b': ['vorm 2', 50, complementair_3],
        'c': ['vorm 3', 75, secundair_1],
        'd': ['vorm 2', 80, secundair_1],
        'e': ['vorm 1', 20, primair_2],
        'f': ['vorm 3', 80, secundair_2],
        'g': ['vorm 1', 10, secundair_2],
        'h': ['vorm 2', 38, secundair_3],
        'i': ['vorm 3', 23, primair_3],
        'j': ['vorm 2', 76, secundair_3],
        'k': ['vorm 1', 12, complementair_1],
        'l': ['vorm 3', 43, complementair_1],
        'm': ['vorm 1', 64, complementair_2],
        'n': ['vorm 2', 64, complementair_2],
        'o': ['vorm 3', 85, primair_4],
        'p': ['vorm 2', 10, primair_3],
        'q': ['vorm 1', 45, primair_3],
        'r': ['vorm 3', 70, primair_4],
        's': ['vorm 1', 36, primair_4],
        't': ['vorm 2', 74, primair_1],
        'u': ['vorm 3', 58, primair_3],
        'v': ['vorm 2', 78, primair_1],
        'w': ['vorm 1', 24, primair_4],
        'x': ['vorm 3', 14, primair_4],
        'y': ['vorm 1', 67, secundair_2],
        'z': ['vorm 2', 70, complementair_2],
        ' ': ['vorm 3', 25, complementair_1],

    }

    global naam, startx, starty
    startx = 0
    starty = 0

    no_stroke()
    teken_achtergrond()

    naam = naam.lower() # Wijzig de invoer naar kleine letters

    bericht = [] # Initialiseer de berichtenlijst

    for letter in naam:
        # Codeer elke letter met een vorm en voeg deze toe aan een lijst
        bericht.append(code[letter])

    for item in bericht:
        if item[0] == 'vorm 1':
            vorm_1(item[1], item[2]) # Teken vorm
            # Vertaal de volgende start-x-coördinaten op basis van de breedte van de vorm
            startx += item[1]
            grootte_controle() # Controleer of je over de zijkant van het venster bent gegaan

        elif item[0] == 'vorm 2':
            vorm_2(item[1], item[2])
            startx += item[1]
            grootte_controle()

        elif item[0] == 'vorm 3':
            vorm_3(item[1], item[2])
            startx += item[1]
            grootte_controle()


print('Voer je naam in om gecodeerde illustraties te maken:')
naam = input()

run(frame_rate=10)
