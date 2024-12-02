import random
game_name = "2048"
valeure_gagnante = 2048

def initialisation(taille):
    #initialise le jeu
    grille = creation_grille(taille)
    creation_tuile(taille, grille)
    return grille

def creation_grille(taille):
    #Creation Grille
    grille = []
    for y in range(taille):
        grille.append([])
        for x in range(taille):
            grille[y].append(0)
    return grille

def creation_tuile(taille, grille):
    #Creation tuile 1
    tuile1 = creation_coordonnées(taille, grille)
    while grille[tuile1[0]][tuile1[1]] != 0:
        tuile1 = creation_coordonnées(taille)
    #Creation tuile 2
    tuile2 = creation_coordonnées(taille, grille)
    while grille[tuile2[0]][tuile2[1]] != 0:
        tuile2 = creation_coordonnées(taille, grille)
    #Verification difference des tuiles 
    while tuile1 == tuile2:
        tuile2 = creation_coordonnées(taille, grille)
    grille[tuile1[0]][tuile1[1]] = random.randrange(2, 5, 2)
    grille[tuile2[0]][tuile2[1]] = random.randrange(2, 5, 2)

def creation_coordonnées(taille, grille):
    x = random.randint(0, taille-1)
    y = random.randint(0, taille-1)
    return [y, x]

def affichage_grille(taille, grille):
    #Affiche grille
    y=0
    for i in range(taille):
        x=0
        #trait
        for j in range(taille*taille+1):
            print("-", end="")
        print()
        #colonne
        for k in range(taille):
            print("|", end="  ")
            if grille[y][x]==0:
                print(" ", end="")
            else:
                print(grille[y][x], end="")
            x+=1
        y+=1
        print("|")
    #trait fin
    for j in range(taille*taille+1):
        print("-", end="")
    print("")

def choix_direction(taille, grille):
    #Demande une direction valide
    direction = input("Entrez la direction : ")
    if direction != "z" and direction != "haut" and direction != "q" and direction != "gauche" and direction != "s" and direction != "bas" and direction != "d" and direction != "droite":
        direction = input("Entree inconnue, veuillez saisir une direction valide : ")
    elif direction == "z" or direction == "haut": return "haut"
    elif direction == "q" or direction == "gauche": return "gauche"
    elif direction == "s" or direction == "bas": return "bas"
    elif direction == "d" or direction == "droite": return "droite"
    
def addition_grille(taille, grille, direction):
    #procedure qui modifie la grille
    tempgrille = grille.copy
    if direction == "gauche" or direction == "q": 
        grille = deplacement_ligne_gauche(taille, grille, tempgrille)
        
    if direction == "droite" or direction == "d": 
        grille = deplacement_ligne_droite(taille, grille, tempgrille)
        
    if direction == "haut" or direction == "z": 
        grille = deplacement_colonne_haut(taille, grille, tempgrille)
        
    if direction == "bas" or direction == "s": 
        grille = deplacement_colonne_bas(taille, grille, tempgrille)
        
    
def deplacement_ligne_gauche(taille, grille, tempgrille):
    for i in range(taille):
        for j in range(taille-1):
            pass
            
def deplacement_ligne_droite(taille, grille, tempgrille):
    for i in range(taille):
        for j in range(taille-1):
            pass
            
def deplacement_colonne_haut(taille, grille, tempgrille):
    for i in range(taille):
        for j in range(taille-1):
            pass    

def deplacement_colonne_bas(taille, grille, tempgrille):
    for i in range(taille):
        for j in range(taille-1):
            pass
        
        

def run_game(taille):
    #deroulement de la partie jusqu'a condition de fin
    #initialisation de la partie
    grille = initialisation(taille)
    affichage_grille(taille, grille)
    #debut du tour par tour
    direction = choix_direction(taille, grille)
    addition_grille(taille, grille, direction)



if __name__ == "__main__":
    run_game(4)