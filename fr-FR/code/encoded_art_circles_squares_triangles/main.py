#!/bin/python3

from p5 import *
from random import randint, seed


def forme_1(taille, couleur): # Chaque forme peut avoir une taille et une couleur différentes en fonction des paramètres

    # Dessine un cercle avec un contour épais

    x = randint(0, 400)
    y = randint(0, 400)
    fill(couleur)
    ellipse(x, y, taille, taille)
    fill(Color(251, 168, 57))
    ellipse(x, y, taille - 20, taille - 20)


def forme_2(taille, couleur):

    # Dessiner un rectangle

    x = randint(0, 400)
    y = randint(0, 400)
    fill(couleur)
    rect(x, y, taille, taille)


def forme_3(taille, couleur): # La taille n'est pas utilisée pour cette fonction mais deux paramètres doivent être passés

    # Dessiner un triangle

    x = randint(0, 400)
    y = randint(0, 400)
    fill(couleur)
    triangle(x, y, x+50, y-100, x+100, y)

# Configurer l'arrière-plan


def dessine_arriere_plan():

    # Couleur de l'arrière-plan
    fill(Color(5, 55, 93))
    rect(0, 0, 400, 400)


def setup():

    size(400, 400)


def draw():

    # -- Ma palette de couleurs -- ## Utiliser les couleurs primaires, secondaires et complémentaires

    # Couleurs primaires

    primaire_1 = Color(14, 92, 151)
    primaire_2 = Color(77, 135, 179)
    primaire_3 = Color(45, 111, 161)
    primaire_4 = Color(8, 71, 120)
    primaire_5 = Color(5, 55, 93)

    # Couleurs secondaires

    secondaire_1 = Color(29, 29, 164)
    secondaire_2 = Color(92, 92, 191)
    secondaire_3 = Color(60, 60, 176)

    # Couleurs complémentaires

    complementaire_1 = Color(234, 137, 8)
    complementaire_2 = Color(255, 188, 99)
    complementaire_3 = Color(251, 168, 57)

    # Dictionnaire des lettres et de leur forme codée avec options de taille et de couleur

    code = {
        'a': ['forme 1', 150, primaire_1],
        'b': ['forme 3', 50, complementaire_3],
        'c': ['forme 3', 75, secondaire_1],
        'd': ['forme 2', 80, secondaire_1],
        'e': ['forme 1', 20, primaire_2],
        'f': ['forme 2', 80, secondaire_2],
        'g': ['forme 1', 10, secondaire_2],
        'h': ['forme 2', 300, secondaire_3],
        'i': ['forme 1', 200, primaire_3],
        'j': ['forme 3', 90, secondaire_3],
        'k': ['forme 1', 12, complementaire_1],
        'l': ['forme 2', 43, complementaire_1],
        'm': ['forme 1', 93, complementaire_2],
        'n': ['forme 2', 64, complementaire_2],
        'o': ['forme 1', 85, primaire_4],
        'p': ['forme 2', 10, primaire_3],
        'q': ['forme 1', 45, primaire_3],
        'r': ['forme 1', 70, primaire_4],
        's': ['forme 1', 36, primaire_4],
        't': ['forme 3', 74, primaire_1],
        'u': ['forme 1', 58, primaire_3],
        'v': ['forme 2', 78, primaire_1],
        'w': ['forme 1', 24, primaire_4],
        'x': ['forme 2', 14, primaire_4],
        'y': ['forme 3', 67, secondaire_2],
        'z': ['forme 2', 70, complementaire_2],
        ' ': ['forme 1', 25, complementaire_1],

    }

    global nom

    seed(10) # Génère les mêmes nombres aléatoires à chaque fois
    no_stroke()
    dessine_arriere_plan()

    nom = nom.lower() # Change l'entrée en minuscule

    message = [] # Initialise la liste des messages

    for lettre in nom:
        # Coder chaque lettre avec une forme et l'ajouter à une liste
        message.append(code[lettre])

    for element in message: # Pour chaque lettre, dessiner la forme choisie
        if element[0] == 'forme 1':
            forme_1(element[1], element[2])
        elif element[0] == 'forme 2':
            forme_2(element[1], element[2])
        elif element[0] == 'forme 3':
            forme_3(element[1], element[2])


print('Entre ton nom pour créer une illustration codée :')
nom = input()

run(frame_rate=10)
