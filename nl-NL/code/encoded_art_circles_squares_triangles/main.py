#!/bin/python3

from p5 import *
from random import randint, seed


def vorm_1(grootte, kleur): # Elke vorm kan een verschillende grootte en kleur hebben op basis van de parameters

    # Tekent een cirkel met een dikke omtrek

    x = randint(0, 400)
    y = randint(0, 400)
    fill(kleur)
    ellipse(x, y, grootte, grootte)
    fill(Color(251, 168, 57))
    ellipse(x, y, grootte - 20, grootte - 20)


def vorm_2(grootte, kleur):

    # Tekent een rechthoek

    x = randint(0, 400)
    y = randint(0, 400)
    fill(kleur)
    rect(x, y, grootte, grootte)


def vorm_3(grootte, kleur): # Grootte wordt niet gebruikt voor deze functie, maar twee parameters moeten worden doorgegeven

    # Tekent een driehoek

    x = randint(0, 400)
    y = randint(0, 400)
    fill(kleur)
    triangle(x, y, x+50, y-100, x+100, y)

# Stel de achtergrond in


def teken_achtergrond():

    # Achtergrondkleur
    fill(Color(5, 55, 93))
    rect(0, 0, 400, 400)


def setup():

    size(400, 400)


def draw():

    # -- Mijn kleurenpalet -- ## Primaire, secundaire en complementaire kleuren gebruiken

    # Primaire kleuren

    primair_1 = Color(14, 92, 151)
    primair_2 = Color(77, 135, 179)
    primair_3 = Color(45, 111, 161)
    primair_4 = Color(8, 71, 120)
    primair_5 = Color(5, 55, 93)

    # Secundaire kleuren

    secundair_1 = Color(29, 29, 164)
    secundair_2 = Color(92, 92, 191)
    secundair_3 = Color(60, 60, 176)

    # Complementaire kleuren

    complementair_1 = Color(234, 137, 8)
    complementair_2 = Color(255, 188, 99)
    complementair_3 = Color(251, 168, 57)

    # Dictionary van letters en hun gecodeerde vorm met grootte- en kleuropties

    code = {
        'a': ['vorm 1', 150, primair_1],
        'b': ['vorm 3', 50, complementair_3],
        'c': ['vorm 3', 75, secundair_1],
        'd': ['vorm 2', 80, secundair_1],
        'e': ['vorm 1', 20, primair_2],
        'f': ['vorm 2', 80, secundair_2],
        'g': ['vorm 1', 10, secundair_2],
        'h': ['vorm 2', 300, secundair_3],
        'i': ['vorm 1', 200, primair_3],
        'j': ['vorm 3', 90, secundair_3],
        'k': ['vorm 1', 12, complementair_1],
        'l': ['vorm 2', 43, complementair_1],
        'm': ['vorm 1', 93, complementair_2],
        'n': ['vorm 2', 64, complementair_2],
        'o': ['vorm 1', 85, primair_4],
        'p': ['vorm 2', 10, primair_3],
        'q': ['vorm 1', 45, primair_3],
        'r': ['vorm 1', 70, primair_4],
        's': ['vorm 1', 36, primair_4],
        't': ['vorm 3', 74, primaire_1],
        'u': ['vorm 1', 58, primair_3],
        'v': ['vorm 2', 78, primair_1],
        'w': ['vorm 1', 24, primair_4],
        'x': ['vorm 2', 14, primair_4],
        'y': ['vorm 3', 67, secundair_2],
        'z': ['vorm 2', 70, complementair_2],
        ' ': ['vorm 1', 25, complementair_1],

    }

    global naam

    seed(10) # Genereer telkens dezelfde willekeurige getallen
    no_stroke()
    teken_achtergrond()

    naam = naam.lower() # Wijzig de invoer naar kleine letters

    bericht = [] # Initialiseer de berichtenlijst

    for letter in naam:
        # Codeer elke letter met een vorm en voeg deze toe aan een lijst
        bericht.append(code[letter])

    for item in bericht: # Teken voor elke letter de gekozen vorm
        if item[0] == 'vorm 1':
            vorm_1(item[1], item[2])
        elif item[0] == 'vorm 2':
            vorm_2(item[1], item[2])
        elif item[0] == 'vorm 3':
            vorm_3(item[1], item[2])


print('Voer je naam in om gecodeerde illustraties te maken:')
naam = input()

run(frame_rate=10)
