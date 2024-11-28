def creer_grille(x):
    return [[0 for i in range(x)] for i in range(x)]


def afficher_grille(grille):
        for ligne in grille:
          print(" | ".join(f"{val:4}" for val in ligne))
          print("-" *25)

        print()


def main():
    try:
        taille = int(input("Entrez la taille de la grille: "))
        if taille < 2:
            print("La taille doit être supérieure ou égale à 2.")
        
        
        grille = creer_grille(taille)
        print("Grille initialisée :")

        afficher_grille(grille)
    
    except ValueError:
        print("Veuillez entrer un entier valide.")
    
if __name__ == "__main__":
    main()

