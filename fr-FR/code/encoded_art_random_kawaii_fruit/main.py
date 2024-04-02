#!/bin/python3

# PROTOTYPE TROIS - DESSINER DES FORMES COMPLEXES APPARAISSANT DE MANIÈRE ALÉATOIRE

from p5 import *
from random import randint, seed


def forme_1(fruit_couleur): # Dessine un fruit Kawaii à une position aléatoire dans la couleur choisie

    # Générer aléatoirement les positions x et y

    x = randint(0, 400)
    y = randint(0, 400)

    brun = Color(200, 120, 0)
    vert = Color(100, 155, 0)

    # Instructions pour dessiner les fruits, quelques calculs sont nécessaires pour que chaque objet apparaisse à l'endroit voulu

    # Corps
    fill(fruit_couleur)
    ellipse(x, y, 100, 95)
    fill(0)
    # Les yeux
    ellipse(x-20, y+10, 15, 15)
    ellipse(x+20, y+10, 15, 15)
    fill(255)
    ellipse(x-18, y+8, 5, 5)
    ellipse(x+22, y+8, 5, 5)
    # La bouche
    fill(0)
    ellipse(x, y+20, 10, 10)
    fill(fruit_couleur)
    ellipse(x, y+18, 10, 10)
    # Zones claires
    fill(255, 70)
    ellipse(x-10, y-20, 20, 20)
    ellipse(x-20, y-15, 15, 15)
    # Tige
    fill(brun)
    triangle(x-5, y-35, x+5, y-75, x+20, y-75)
    fill(vert)
    push_matrix()
    translate(x-20, y-55)
    rotate(radians(45))
    ellipse(0, 0, 40, 15)
    pop_matrix()


def forme_2(fruit_couleur): # Dessine un fruit citron  dans une couleur choisie à une position aléatoire

    x = randint(0, 400)
    y = randint(0, 400)

    brun = Color(200, 120, 0)
    vert = Color(100, 155, 0)

    # Instructions pour dessiner le citron

    # Corps
    fill(fruit_couleur)
    ellipse(x, y, 110, 150)
    ellipse(x, y+70, 30, 30)
    ellipse(x, y-70, 30, 30)
    fill(0)
    # Les yeux
    ellipse(x-20, y, 15, 15)
    ellipse(x+20, y, 15, 15)
    fill(255)
    ellipse(x-18, y-3, 5, 5)
    ellipse(x+22, y-3, 5, 5)
    # La bouche
    fill(0)
    ellipse(x, y+12, 10, 10)
    fill(fruit_couleur)
    ellipse(x, y+10, 10, 10)
    # Zones claires
    fill(255, 70)
    ellipse(x-10, y-40, 20, 20)
    ellipse(x-20, y-35, 15, 15)
    # Tige
    fill(brun)
    triangle(x-15, y-65, x-5, y-100, x+10, y-100)
    fill(vert)
    push_matrix()
    translate(x-30, y-80)
    rotate(radians(45))
    ellipse(0, 0, 40, 15)
    pop_matrix()


def forme_3(fruit_couleur): # Dessine une cerise dans une couleur choisie et une position aléatoire

    x = randint(0, 400)
    y = randint(0, 400)

    brun = Color(200, 120, 0)
    vert = Color(100, 155, 0)

    # Instructions pour dessiner la cerise

    # Corps
    fill(fruit_couleur)
    ellipse(x, y, 70, 70)
    # Zones claires
    fill(255, 70)
    ellipse(x, y, 60, 60)
    fill(fruit_couleur)
    ellipse(x+3, y+3, 60, 60)
    # Les yeux
    fill(0)
    ellipse(x-15, y, 15, 15)
    ellipse(x+15, y, 15, 15)
    fill(255)
    ellipse(x-13, y-3, 5, 5)
    ellipse(x+18, y-3, 5, 5)
    # La bouche
    fill(0)
    ellipse(x, y+12, 10, 10)
    fill(fruit_couleur)
    ellipse(x, y+10, 10, 10)
    # Tige
    fill(brun)
    triangle(x-5, y-20, x+5, y-80, x+10, y-80)
    # Feuilles
    fill(vert)
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

# Ajoute une couleur d'arrière-plan


def dessine_arriere_plan():

    # Couleur de l'arrière-plan
    fill(Color(255, 255, 255))
    rect(0, 0, 400, 400)


def setup():

    size(400, 400)


def draw():

    # Palette de couleurs pour les dessins de fruits

    orange = Color(255, 165, 0)
    citron = Color(134, 229, 77)
    cerise = Color(213, 17, 70)
    rouge = Color(229, 86, 77)
    bleu = Color(85, 182, 225)
    violet = Color(165, 131, 245)
    jaune = Color(243, 247, 32)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    surprise_moi = Color(r, g, b) # Génère une couleur aléatoire

    # Dictionnaire des lettres et de leur forme codée, une couleur est sélectionnée dans la palette

    code = {
        'a': ['forme 3', cerise],
        'b': ['forme 1', orange],
        'c': ['forme 1', citron],
        'd': ['forme 1', bleu],
        'e': ['forme 3', rouge],
        'f': ['forme 1', surprise_moi],
        'g': ['forme 1', violet],
        'h': ['forme 1', violet],
        'i': ['forme 3', violet],
        'j': ['forme 1', rouge],
        'k': ['forme 2', violet],
        'l': ['forme 1', rouge],
        'm': ['forme 1', violet],
        'n': ['forme 1', violet],
        'o': ['forme 1', rouge],
        'p': ['forme 2', citron],
        'q': ['forme 1', bleu],
        'r': ['forme 3', surprise_moi],
        's': ['forme 1', orange],
        't': ['forme 2', jaune],
        'u': ['forme 1', jaune],
        'v': ['forme 1', jaune],
        'w': ['forme 1', rouge],
        'x': ['forme 2', surprise_moi],
        'y': ['forme 1', bleu],
        'z': ['forme 1', citron],
        ' ': ['forme 2', cerise],

    }

    global nom, seed_value, count

    seed(seed_value) # Génère les mêmes nombres aléatoires à chaque fois
    no_stroke()
    dessine_arriere_plan()

    nom = nom.lower() # Change l'entrée en minuscule

    message = [] # Initialise la liste des messages

    for lettre in nom:
        # Coder chaque lettre avec une forme et l'ajouter à une liste
        message.append(code[lettre])

    for element in message : # Dessiner soit la forme 1, 2 ou 3 avec l'option de couleur sélectionnée
        if element[0] == 'forme 1':
            forme_1(element[1])
        elif element[0] == 'forme 2':
            forme_2(element[1])
        elif element[0] == 'forme 3':
            forme_3(element[1])

    if count >= 1:
        print('Appuie sur la touche Entrée pour redessiner un autre motif :')
        reponse = input()
        if reponse == '':
            seed_value = randint(0, 100)

    count = 1


seed_value = 10
count = 0
print('Entre ton nom pour réaliser une œuvre d\'art codée :')
nom = input()

run(frame_rate=10)
