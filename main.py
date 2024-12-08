import random

game_name = "2048"
valeure_gagnante = 2048

# Initialisation du jeu
def initialisation(taille):
    grille = creation_grille(taille)
    creation_tuile(taille, grille)
    return grille

# Création de la grille vide
def creation_grille(taille):
    grille = []
    for y in range(taille):
        grille.append([0] * taille)
    return grille

# Création de deux tuiles de départ
def creation_tuile(taille, grille):
    # Recherche des cases vides
    cases_vides = [(y, x) for y in range(taille) for x in range(taille) if grille[y][x] == 0]
    if cases_vides:
        y, x = random.choice(cases_vides)
        grille[y][x] = random.choice([2, 4])

# Affiche la grille
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
            print("|", end="")
            if grille[y][x]==0:
                print(" ", end="  ")
            else:
                if grille[y][x]>=10:
                    
                    print(" ", end="")
                    print(grille[y][x], end="")
                else:
                    print("  ", end="")
                    print(grille[y][x], end="")
            x+=1
        y+=1
        print("|")
    #trait fin
    for j in range(taille*taille+1):
        print("-", end="")
    print("")

# Demande une direction valide
def choix_direction():
    directions = {
        "z": "haut", "haut": "haut", 
        "q": "gauche", "gauche": "gauche", 
        "s": "bas", "bas": "bas", 
        "d": "droite", "droite": "droite"
    }
    while True:
        direction = input("Entrez la direction (z/q/s/d ou haut/gauche/bas/droite) : ").lower()
        if direction in directions:
            return directions[direction]
        print("Direction invalide, réessayez.")

# Déplace et fusionne les tuiles
def addition_grille(taille, grille, direction):
    if direction == "gauche":
        deplacement_ligne_gauche(taille, grille)
    elif direction == "droite":
        deplacement_ligne_droite(taille, grille)
    elif direction == "haut":
        deplacement_colonne_haut(taille, grille)
    elif direction == "bas":
        deplacement_colonne_bas(taille, grille)

# Déplacement vers la gauche
def deplacement_ligne_gauche(taille, grille):
    for i in range(taille):
        ligne = [x for x in grille[i] if x != 0]
        for j in range(len(ligne)-1):
            if ligne[j] == ligne[j+1]:
                ligne[j] *= 2
                ligne[j+1] = 0
        grille[i] = [x for x in ligne if x != 0] + [0] * (taille - len([x for x in ligne if x != 0]))

# Déplacement vers la droite
def deplacement_ligne_droite(taille, grille):
    for i in range(taille):
        ligne = [x for x in grille[i] if x != 0]
        for j in range(len(ligne)-1, 0, -1):
            if ligne[j] == ligne[j-1]:
                ligne[j] *= 2
                ligne[j-1] = 0
        grille[i] = [0] * (taille - len([x for x in ligne if x != 0])) + [x for x in ligne if x != 0]

# Déplacement vers le haut
def deplacement_colonne_haut(taille, grille):
    for j in range(taille):
        colonne = [grille[i][j] for i in range(taille) if grille[i][j] != 0]
        for i in range(len(colonne)-1):
            if colonne[i] == colonne[i+1]:
                colonne[i] *= 2
                colonne[i+1] = 0
        colonne = [x for x in colonne if x != 0] + [0] * (taille - len([x for x in colonne if x != 0]))
        for i in range(taille):
            grille[i][j] = colonne[i]

# Déplacement vers le bas
def deplacement_colonne_bas(taille, grille):
    for j in range(taille):
        colonne = [grille[i][j] for i in range(taille) if grille[i][j] != 0]
        for i in range(len(colonne)-1, 0, -1):
            if colonne[i] == colonne[i-1]:
                colonne[i] *= 2
                colonne[i-1] = 0
        colonne = [0] * (taille - len([x for x in colonne if x != 0])) + [x for x in colonne if x != 0]
        for i in range(taille):
            grille[i][j] = colonne[i]

# Vérifie si le joueur a gagné
def tester_gagner(grille):
    for ligne in grille:
        if valeure_gagnante in ligne:
            return True
    return False

# Vérifie si le joueur a perdu
def tester_perdu(grille, taille):
    for i in range(taille):
        for j in range(taille):
            # Vérifie s'il y a une case vide
            if grille[i][j] == 0:
                return False
            # Vérifie les cases adjacentes (droite et bas uniquement)
            if j < taille - 1 and grille[i][j] == grille[i][j+1]:
                return False
            if i < taille - 1 and grille[i][j] == grille[i+1][j]:
                return False
    return True

# Déroulement de la partie
def run_game(taille):
    grille = initialisation(taille)
    perdu = False
    while not perdu:
        affichage_grille(taille, grille)
        if tester_gagner(grille):
            print("Félicitations, vous avez atteint 2048!")
            break
        if tester_perdu(grille, taille):
            print("Game over! Plus de mouvements possibles.")
            perdu = True
            break
        direction = choix_direction()
        ancienne_grille = [ligne[:] for ligne in grille]
        addition_grille(taille, grille, direction)
        if ancienne_grille != grille:
            creation_tuile(taille, grille)

# Lancement du jeu
if __name__ == "__main__":
    run_game(4)
