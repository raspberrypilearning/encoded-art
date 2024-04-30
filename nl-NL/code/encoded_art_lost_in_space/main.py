#!/bin/python3

from p5 import *
from random import randint, seed

# Teken een planeet op basis van de gekozen grootte en kleur


def vorm_1(grootte, kleur):

    x = randint(0, 400)
    y = randint(0, 400)
    if kleur == 'paars':
        image(paarse_planeet, x, y, grootte, grootte)
    elif kleur == 'oranje':
        image(oranje_planeet, x, y, grootte, grootte)
    elif kleur == 'groen':
        image(groene_planeet, x, y, grootte, grootte)
    elif kleur == 'grijs':
        image(grijze_maan, x, y, grootte, grootte)

# Teken een ruimteobject op basis van het gekozen object en de grootte


def vorm_2(grootte, kleur):

    x = randint(0, 400)
    y = randint(0, 400)
    if object == 'satelliet':
        image(satelliiet, x, y, grootte, grootte)
    elif object == 'astronaut':
        image(astronaut, x, y, grootte, grootte)
    elif object == 'astropi':
        image(astropi, x, y, grootte, grootte)

# Teken een ster op basis van de gekozen kleur en afmeting


def vorm_3(grootte, kleur):

    x = randint(0, 400)
    y = randint(0, 400)
    if kleur == 'geel':
        image(gele_ster, x, y, grootte, grootte)
    elif kleur == 'roze':
        image(roze_ster, x, y, grootte, grootte)
    elif kleur == 'blauw':
        image(blauwe_ster, x, y, grootte, grootte)

# Voegt een achtergrondkleur toe


def teken_achtergrond():

    # Achtergrondkleur
    fill(Color(0, 0, 0))
    rect(0, 0, 400, 400)


def setup():

    # Geef andere functies toegang tot de afbeeldingen
    global paarse_planeet, oranje_planeet, groene_planeet, astropi, astronaut, satelliet
    global grijze_maan, gele_ster, roze_ster, blauwe_ster

    size(400, 400)

    # Laad de benodigde afbeeldingen in variabelen
    paarse_planeet = load_image('purple_planet.png')
    oranje_planeet = load_image('orange_planet.png')
    groene_planeet = load_image('green_planet.png')
    astropi = load_image('astropi.png')
    astronaut = load_image('astronaut.png')
    satelliet = load_image('satellite.png')
    grijze_maan = load_image('moon.png')
    gele_ster = load_image('yellow_star.png')
    roze_ster = load_image('pink_star.png')
    blauwe_ster = load_image('blue_star.png')


def draw():

    # Dictionary van letters en hun gecodeerde vorm
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
        ' ': ['vorm 3', 25, 'roze'],
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

    for item in bericht: # Voor elke letter in het bericht, teken een vorm
        if item[0] == 'vorm 1':
            vorm_1(item[1], item[2])
        elif item[0] == 'vorm 2':
            vorm_2(item[1], item[2])
        elif item[0] == 'vorm 3':
            vorm_3(item[1], item[2])


print('Voer je naam in om gecodeerde illustraties te maken:')
naam = input()

run(frame_rate=10)
