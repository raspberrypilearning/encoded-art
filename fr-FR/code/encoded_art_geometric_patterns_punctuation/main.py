#!/bin/python3

# PROTOTYPE QUATRE - ART D'INSPIRATION AFRICAINE

from p5 import *


def taille_test(): # Vérifie si tu es sorti du côté de la fenêtre

    global startx
    global starty
    if startx >= 400:
        startx = 0
        starty += 80


def forme_1(taille, couleur): # Dessine un diamant

    global startx
    global starty
    x1 = startx
    y1 = starty + 40 # Déplacer au centre de la bande
    x2 = x1 + (taille/2)
    y2 = y1 + (taille/2)
    x3 = x1 + taille
    y3 = y1
    x4 = x1 + (taille/2)
    y4 = y1 - (taille/2)
    fill(couleur)
    quad(x1, y1, x2, y2, x3, y3, x4, y4)


def forme_2(taille, couleur): # Dessine un carré

    global startx
    global starty
    x = startx
    y = starty
    fill(couleur)
    rect(x, y, taille, taille)


def forme_3(taille, couleur): # Dessine un triangle

    global startx
    global starty
    x1 = startx
    y1 = starty
    x2 = x1 + (taille/2)
    y2 = y1 + taille
    x3 = x1 + taille
    y3 = y1
    fill(couleur)
    triangle(x1, y1, x2, y2, x3, y3)


# Ajoute une couleur d'arrière-plan
def dessine_arriere_plan():

    # Couleurs d’arrière-plan
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

    # -- Ma palette de couleurs --

    # Couleurs primaires

    primaire_1 = Color(246, 32, 100)
    primaire_2 = Color(247, 0, 79)
    primaire_3 = Color(234, 0, 75)
    primaire_4 = Color(196, 0, 63)
    primaire_5 = Color(4, 0, 1)

    # Couleurs secondaires

    secondaire_1 = Color(255, 198, 33)
    secondaire_2 = Color(255, 190, 0)
    secondaire_3 = Color(55, 190, 0)

    # Couleurs complémentaires

    complementaire_1 = Color(59, 63, 230)
    complementaire_2 = Color(5, 9, 154)
    complementaire_3 = Color(133, 246, 32)

    code = {
        'a': ['forme 1', 80, primaire_1],
        'b': ['forme 2', 50, complementaire_3],
        'c': ['forme 3', 75, secondaire_1],
        'd': ['forme 2', 80, secondaire_1],
        'e': ['forme 1', 20, primaire_2],
        'f': ['forme 3', 80, secondaire_2],
        'g': ['forme 1', 10, secondaire_2],
        'h': ['forme 2', 38, secondaire_3],
        'i': ['forme 3', 23, primaire_3]
        'j': ['forme 2', 76, secondaire_3],
        'k': ['forme 1', 12, complementaire_1],
        'l': ['forme 3', 43, complementaire_1],
        'm': ['forme 1', 64, complementaire_2],
        'n': ['forme 2', 64, complementaire_2],
        'o': ['forme 3', 85, primaire_4],
        'p': ['forme 2', 10, primaire_3],
        'q': ['forme 1', 45, primaire_3],
        'r': ['forme 3', 70, secondaire_3],
        's': ['forme 1', 36, primaire_4],
        't': ['forme 2', 74, primaire_1],
        'u': ['forme 3', 58, primaire_3],
        'v': ['forme 2', 78, primaire_1],
        'w': ['forme 1', 24, secondaire_3],
        'x': ['forme 3', 14, primaire_4],
        'y': ['forme 1', 67, secondaire_2],
        'z': ['forme 2', 70, complementaire_2],
        ' ': ['forme 3', 25, complementaire_1],
        '?': ['forme 2', 54, secondaire_2],
        '!': ['forme 3', 37, primaire_4],
        '#': ['forme 2', 76, secondaire_1],
        '@': ['forme 1', 24, primaire_3],
        '£': ['forme 3', 83, secondaire_2],
        '$': ['forme 1', 72, secondaire_3],
        ':': ['forme 2', 54, primaire_1],
        '&': ['forme 3', 63, secondaire_2],
        '*': ['forme 2', 14, secondaire_3],
        '+': ['forme 1', 39, secondaire_1],
        '=': ['forme 3', 75, primaire_4],
        '-': ['forme 1', 79, secondaire_2],
        '~': ['forme 2', 38, complementaire_2],
        '/': ['forme 3', 25, complementaire_1],

    }

    global nom, startx, starty
    startx = 0
    starty = 0

    no_stroke()
    dessine_arriere_plan()

    nom = nom.lower() # Change l'entrée en minuscule

    message = [] # Initialise la liste des messages

    for lettre in nom:
        # Coder chaque lettre avec une forme et l'ajouter à une liste
        message.append(code[lettre])

    for element in message:
        if element[0] == 'forme 1':
            forme_1(element[1], element[2]) # Dessiner une forme
            # Déplacer la prochaine coordonnée x de départ par la largeur de la forme
            startx += element[1]
            taille_test(): # Vérifie si tu es sorti du côté de la fenêtre

        elif element[0] == 'forme 2':
            forme_2(element[1], element[2])
            startx += element[1]
            taille_test()

        elif element[0] == 'forme 3':
            forme_3(element[1], element[2])
            startx += element[1]
            taille_test()


print('Entre ton nom pour réaliser une œuvre d'art codée :')
nom = input()

run(frame_rate=10)
