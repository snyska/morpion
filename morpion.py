grille=[["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]

nbr_reference=("0,1","1,0","0,2","2,0","1,2","2,1","0,0","1,1","2,2")


def afficher_grille(grille):
    print("\n  0   1   2")  
    for i in range(3):
        ligne = f"{i} " + " | ".join(grille[i])
        print(ligne)
    
        if i < 2:
            print("  ---------")
    print()  


def win(grille,symbole):
    
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == symbole:
            return True
    
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == symbole:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    
    
def lancement(x):
    while True:
        while True:
            c= input("Choisis l'emplacement (ex: 0,1) : ")
            if c in nbr_reference:
                break
            else:
                print("choix invalide")
        coordoner = c.split(",")
        i= int(coordoner[0])
        j = int(coordoner[1])
        if  grille[i][j] == "_":
            grille[i][j] = x
            break
        else:
            print("choix invalide")
   
    

def morpion():
    afficher_grille(grille)
    lancement("O")
    for _ in range(4):
        afficher_grille(grille)
        lancement("X")
        if win(grille,"X"):
            afficher_grille(grille)
            return ("le X a gagner !!")
        afficher_grille(grille)
        lancement("O")
        if win(grille,"O"):
            afficher_grille(grille)
            return ("le O a gagner !!")
    return ("match nul ☻")

    
    
print(morpion())