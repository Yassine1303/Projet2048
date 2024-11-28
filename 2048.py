import random

def initialisation(taille):
    grille = creation_grille(taille)
    creation_tuile(taille)
    return grille

def creation_grille(taille):
    #Creation Grille
    grille = []
    for y in range(taille):
        grille.append([])
        for x in range(taille):
            grille[y].append(" ")
    return grille

def creation_tuile(taille):
    #Creation Tuile 1
    tuile1 = creation_coordonnées(taille)
    tuile2 = creation_coordonnées(taille)
    #Verification difference des tuiles 
    while tuile1 == tuile2:
        tuile2 = creation_coordonnées(taille)
    return [tuile1, tuile2]

def creation_coordonnées(taille):
    x = random.randint(0, taille)
    y = random.randint(0, taille)
    return [x, y]


def run_game(taille):
    grille = initialisation(taille)


if __name__ == "__main__":
    run_game(4)