#!/bin/python3

# PROTOTYPE DRIE - COMPLEXE VORMEN TEKENEN DIE WILLEKEURIG VERSCHIJNEN

from p5 import *
from random import randint, seed


def vorm_1(fruit_kleur): # Tekent een Kawaii-fruit op een willekeurige positie in de gekozen kleur

    # Genereer willekeurig de x- en y-posities

    x = randint(0, 400)
    y = randint(0, 400)

    bruin = Color(200, 120, 0)
    groen = Color(100, 155, 0)

    # Instructies om het fruit te tekenen, met wat wiskunde die nodig is om elk object te laten verschijnen op de juiste plek

    # Lichaam
    fill(fruit_kleur)
    ellipse(x, y, 100, 95)
    fill(0)
    # Ogen
    ellipse(x-20, y+10, 15, 15)
    ellipse(x+20, y+10, 15, 15)
    fill(255)
    ellipse(x-18, y+8, 5, 5)
    ellipse(x+22, y+8, 5, 5)
    # Mond
    fill(0)
    ellipse(x, y+20, 10, 10)
    fill(fruit_kleur)
    ellipse(x, y+18, 10, 10)
    # Highlights
    fill(255, 70)
    ellipse(x-10, y-20, 20, 20)
    ellipse(x-20, y-15, 15, 15)
    # Steel
    fill(bruin)
    triangle(x-5, y-35, x+5, y-75, x+20, y-75)
    fill(groen)
    push_matrix()
    translate(x-20, y-55)
    rotate(radians(45))
    ellipse(0, 0, 40, 15)
    pop_matrix()


def vorm_2(fruit_kleur): # Tekent een limoen in een gekozen kleur op een willekeurige positie

    x = randint(0, 400)
    y = randint(0, 400)

    bruin = Color(200, 120, 0)
    groen = Color(100, 155, 0)

    # Instructies voor het tekenen van de limoen

    # Lichaam
    fill(fruit_kleur)
    ellipse(x, y, 110, 150)
    ellipse(x, y+70, 30, 30)
    ellipse(x, y-70, 30, 30)
    fill(0)
    # Ogen
    ellipse(x-20, y, 15, 15)
    ellipse(x+20, y, 15, 15)
    fill(255)
    ellipse(x-18, y-3, 5, 5)
    ellipse(x+22, y-3, 5, 5)
    # Mond
    fill(0)
    ellipse(x, y+12, 10, 10)
    fill(fruit_kleur)
    ellipse(x, y+10, 10, 10)
    # Highlights
    fill(255, 70)
    ellipse(x-10, y-40, 20, 20)
    ellipse(x-20, y-35, 15, 15)
    # Steel
    fill(bruin)
    triangle(x-15, y-65, x-5, y-100, x+10, y-100)
    fill(groen)
    push_matrix()
    translate(x-30, y-80)
    rotate(radians(45))
    ellipse(0, 0, 40, 15)
    pop_matrix()


def vorm_3(fruit_kleur): # Tekent een kers in een gekozen kleur en een willekeurige positie

    x = randint(0, 400)
    y = randint(0, 400)

    bruin = Color(200, 120, 0)
    groen = Color(100, 155, 0)

    # Instructies voor het tekenen van de kers

    # Lichaam
    fill(fruit_kleur)
    ellipse(x, y, 70, 70)
    # Highlights
    fill(255, 70)
    ellipse(x, y, 60, 60)
    fill(fruit_kleur)
    ellipse(x+3, y+3, 60, 60)
    # Ogen
    fill(0)
    ellipse(x-15, y, 15, 15)
    ellipse(x+15, y, 15, 15)
    fill(255)
    ellipse(x-13, y-3, 5, 5)
    ellipse(x+18, y-3, 5, 5)
    # Mond
    fill(0)
    ellipse(x, y+12, 10, 10)
    fill(fruit_kleur)
    ellipse(x, y+10, 10, 10)
    # Steel
    fill(bruin)
    triangle(x-5, y-20, x+5, y-80, x+10, y-80)
    # Blaadjes
    fill(groen)
    push_matrix()
    translate(x-10, y-35)
    rotate(radians(45))
    ellipse(0, 0, 30, 15)
    pop_matrix()
    fill(Color(15, 140, 12))
    push_matrix()
    translate(x-10, y-35)
    rotate(radians(110))
    ellipse(-10, -15, 30, 15)
    pop_matrix()

# Voegt een achtergrondkleur toe


def teken_achtergrond():

    # Achtergrondkleur
    fill(Color(255, 255, 255))
    rect(0, 0, 400, 400)


def setup():

    size(400, 400)


def draw():

    # Kleurpalet voor het tekenen van fruit

    oranje = Color(255, 165, 0)
    limoen = Color(134, 229, 77)
    kers = Color(213, 17, 70)
    rood = Color(229, 86, 77)
    blauw = Color(85, 182, 225)
    paars = Color(165, 131, 245)
    geel = Color(243, 247, 32)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    verras_me = Color(r, g, b) # Genereert een willekeurige kleur

    # Dictionary van letters en hun gecodeerde vorm, er wordt een kleur geselecteerd uit het palet

    code = {
        'a': ['vorm 3', kers],
        'b': ['vorm 1', oranje],
        'c': ['vorm 1', limoen],
        'd': ['vorm 1', blauw],
        'e': ['vorm 3', rood],
        'f': ['vorm 1', verras_me],
        'g': ['vorm 1', paars],
        'h': ['vorm 1', paars],
        'i': ['vorm 3', paars],
        'j': ['vorm 1', rood],
        'k': ['vorm 2', paars],
        'l': ['vorm 1', rood],
        'm': ['vorm 1', paars],
        'n': ['vorm 1', paars],
        'o': ['vorm 1', rood],
        'p': ['vorm 2', limoen],
        'q': ['vorm 1', blauw],
        'r': ['vorm 3', verras_me],
        's': ['vorm 1', oranje],
        't': ['vorm 2', geel],
        'u': ['vorm 1', geel],
        'v': ['vorm 1', geel],
        'w': ['vorm 1', rood],
        'x': ['vorm 2', verras_me],
        'y': ['vorm 1', blauw],
        'z': ['vorm 1', limoen],
        ' ': ['vorm 2', kers],

    }

    global naam, seed_waarde, aantal

    seed(seed_waarde) # Genereer elke keer dezelfde willekeurige getallen
    no_stroke()
    teken_achtergrond()

    naam = naam.lower() # Wijzig de invoer naar kleine letters

    bericht = [] # Initialiseer de berichtenlijst

    for letter in naam:
        # Codeer elke letter met een vorm en voeg deze toe aan een lijst
        bericht.append(code[letter])

    for item in bericht: # Teken vorm 1, 2 of 3 met de geselecteerde kleuroptie
        if item[0] == 'vorm 1':
            vorm_1(item[1])
        elif item[0] == 'vorm 2':
            vorm_2(item[1])
        elif item[0] == 'vorm 3':
            vorm_3(item[1])

    if aantal >= 1:
        print('Druk op Enter om opnieuw te tekenen in een ander patroon:')
        antwoord = input()
        if antwoord == '':
            seed_waarde = randint(0, 100)

    aantal = 1


seed_waarde = 10
aantal = 0
print('Voer je naam in om gecodeerde illustraties te maken:')
naam = input()

run(frame_rate=10)
