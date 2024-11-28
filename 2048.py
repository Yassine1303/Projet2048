import random

def initialisation(taille):
    creation_grille(taille)
    creation_tuile(taille)

def creation_grille(taille):
    #Creation Grille
    grille = []
    for y in range(taille):
        grille.append([])
        for x in range(taille):
            grille[y].append(" ")
    print(grille)
    return grille

def creation_tuile(taille):
    #Creation Tuile
    tuile1 = random.randint(0, taille)
    tuile2 = random.randint(0, taille)
    while tuile1 == tuile2:
        tuile2 = random.randint(2, 4, 2)
    return 
    



def run_game(taille):
    creation_grille(taille)

if __name__ == "__main__":
    run_game(4)