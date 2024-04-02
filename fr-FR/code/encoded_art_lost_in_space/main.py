#!/bin/python3

from p5 import *
from random import randint, seed

# Dessiner une planète en fonction de la taille et de la couleur choisies


def forme_1(taille, couleur):

    x = randint(0, 400)
    y = randint(0, 400)
    if couleur == 'violet':
        image(planete_violette, x, y, taille, taille)
    elif couleur == 'orange':
        image(planete_orange, x, y, taille, taille)
    elif couleur == 'vert':
        image(planete_verte, x, y, taille, taille)
    elif couleur == 'gris':
        image(lune_grise, x, y, taille, taille)

# Dessine un objet spatial en fonction de l'objet et de la taille choisis


def forme_2(taille, objet):

    x = randint(0, 400)
    y = randint(0, 400)
    if objet == 'satellite':
        image(satellite, x, y, taille, taille)
    elif objet == 'astronaute':
        image(astronaute, x, y, taille, taille)
    elif objet == 'astropi':
        image(astropi, x, y, taille, taille)

# Dessiner une étoile en fonction de la couleur et de la taille choisies


def forme_3(taille, couleur):

    x = randint(0, 400)
    y = randint(0, 400)
    if couleur == 'jaune':
        image(etoile_jaune, x, y, taille, taille)
    elif couleur == 'rose':
        image(etoile_rose, x, y, taille, taille)
    elif couleur == 'bleu':
        image(etoile_bleue, x, y, taille, taille)

# Ajoute une couleur d'arrière-plan


def dessine_arriere_plan():

    # Couleur de l'arrière-plan
    fill(Color(0, 0, 0))
    rect(0, 0, 400, 400)


def setup():

    # Autoriser d'autres fonctions à accéder aux images
    global planete_violette, planete_orange, planete_verte, astropi, astronaute, satellite
    global lune_grise, etoile_jaune, etoile_rose, etoile_bleue

    size(400, 400)

    # Charger les images nécessaires dans les variables
    planete_violette = load_image('purple_planet.png')
    planete_orange = load_image('orange_planet.png')
    planete_verte = load_image('green_planet.png')
    astropi = load_image('astropi.png')
    astronaute = load_image('astronaut.png')
    satellite = load_image('satellite.png')
    lune_grise = load_image('moon.png')
    etoile_jaune = load_image('yellow_star.png')
    etoile_rose = load_image('pink_star.png')
    etoile_bleue = load_image('blue_star.png')


def draw():

    # Dictionnaire des lettres et leur forme codée
    code = {
        'a': ['forme 3', 150, 'rose'],
        'b': ['forme 3', 50, 'jaune'],
        'c': ['forme 2', 75, 'astonaute'],
        'd': ['forme 2', 80, 'astropi'],
        'e': ['forme 1', 20, 'orange'],
        'f': ['forme 2', 80, 'satellite'],
        'g': ['forme 1', 10, 'violet'],
        'h': ['forme 1', 300, 'vert'],
        'i': ['forme 1', 200, 'orange'],
        'j': ['forme 2', 90, 'astropi'],
        'k': ['forme 1', 12, 'violet'],
        'l': ['forme 3', 43, 'rose'],
        'm': ['forme 1', 93, 'orange'],
        'n': ['forme 1', 64, 'vert'],
        'o': ['forme 3', 85, 'bleu'],
        'p': ['forme 2', 10, 'astropi'],
        'q': ['forme 3', 45, 'bleu'],
        'r': ['forme 1', 70, 'violet'],
        's': ['forme 1', 36, 'orange'],
        't': ['forme 2', 74, 'astronaute'],
        'u': ['forme 1', 58, 'gris'],
        'v': ['forme 3', 78, 'jaune'],
        'w': ['forme 1', 24, 'orange'],
        'x': ['forme 2', 14, 'astropi'],
        'y': ['forme 1', 67, 'violet'],
        'z': ['forme 2', 70, 'astropi'],
        ' ': ['forme 3', 25, 'rose'],
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

    for element in message : # Pour chaque lettre dans le message, dessiner une forme
        if element[0] == 'forme 1':
            forme_1(element[1], element[2])
        elif element[0] == 'forme 2':
            forme_2(element[1], element[2])
        elif element[0] == 'forme 3':
            forme_3(element[1], element[2])


print('Entre ton nom pour réaliser une œuvre d\'art codée :')
nom = input()

run(frame_rate=10)
