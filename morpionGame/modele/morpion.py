def afficherMorpion(tablemorpion):
    for i in range(3):
        for j in range(3):
            print(tablemorpion[i][j])

def verifierSiJoueurAGagner(nomjoueur, tablemorpion):
    matricecoordonnee = collecterLesCoordonneesPions(nomjoueur,tablemorpion)
    return siPionAligne(matricecoordonnee)

def collecterLesCoordonneesPions(nomjoueur, tablemorpion):
    matricecoordonnee=[]
    for ligne in range(len(tablemorpion)):
        for colonne in range(len(tablemorpion)):
            if(nomjoueur==tablemorpion[ligne][colonne]):
                print(ligne,colonne)
                matricecoordonnee.append((ligne,colonne))

    return matricecoordonnee

def siPionAligne(matricecoordonnee):
    if(len(matricecoordonnee)!=3):
        return False
    elif matricecoordonnee[0][0] == matricecoordonnee[1][0]:
        return matricecoordonnee[2][0] == matricecoordonnee[1][0]
    elif matricecoordonnee[0][1] == matricecoordonnee[1][1]:
        return matricecoordonnee[1][1] == matricecoordonnee[2][1]
    elif matricecoordonnee[0][0] == matricecoordonnee[0][1]:
        return matricecoordonnee[1][0] == matricecoordonnee[1][1] and matricecoordonnee[2][0] == matricecoordonnee[2][1]

def verifierNombreCaseRestante(tablemorpion):
    compteur = 0
    for liste in tablemorpion:
        for element in liste:
            if element == "":
                compteur += 1
    return compteur


def verifierSiUneSeuleCaseReste(tablemorpion):
    if verifierNombreCaseRestante(tablemorpion) == 1:
        return
    return False


def saisirCoordonneesCase(nomjoueur):
    print(f"Joueur {nomjoueur},Veuillez suivre les intrcutions de saisie ou saisir 8 pour quitter la saisie")
    ligne = saisirCoordonne("Ligne")
    colonne = saisirCoordonne("colonne")
    return ligne, colonne


def saisirCoordonne(axe):
    fin = False
    while (fin == False):
        coordonnee = int(input(f"Saisir le numéro de la {axe}: "))
        if verifierInputLige(coordonnee):
            return coordonnee
        print(f"La coordonnee de la {axe}")


""" 
Methode pour verifier la coordonnee rentré pour le contenir dans
--coordonnee : est le nombre saisi a vérifier
"""


def verifierInputLige(coordonnee):
    if 0 <= coordonnee < 3:
        return True
    return False


def poserPion(tablemorpion, nomjouer):
    """Joueur X choisi sa case"""
    while (True):
        ligne, colonne = saisirCoordonneesCase(nomjouer)
        if not siCaseOccupe(ligne, colonne, tablemorpion):
            tablemorpion[ligne][colonne] = nomjouer
            return tablemorpion
        print("Cette case Est occpé.")


def siCaseOccupe(ligne, colonne, tablemorpion):
    return tablemorpion[ligne][colonne] != ""


def jouerPartie(tablemorpion):
    while (True):
        tablemorpion = poserPion(tablemorpion, "X")
        print(tablemorpion)

        if verifierSiJoueurAGagner("X", tablemorpion):
            return "X"
        tablemorpion = poserPion(tablemorpion, "O")
        print(tablemorpion)

        if verifierSiJoueurAGagner("O", tablemorpion):
            return "O"
        if verifierSiUneSeuleCaseReste(tablemorpion):
            return "null"



def main():
    """ Section inilisatino des données """

    """Morpiontable """
    tablemorpion = [["", "", ""], ["", "", ""], ["", "", ""]]
    print("Bienvenu dans le jeu Morpion avec deux joueurs O et X qu i vont s'affronter dans une partie")
    """début de la boucle de partie"""
    while (True):
        print("Veuillez Saisir :\n" + "Y : pour lancer un nouvelle Partie\n" + "N : Pour Quitter le jeur \n" +
              "PS: VEUILLEZ RESPECTER LA CASSE")
        resultat = ""
        partie = input()
        if (partie == "Y"):
            resultat = jouerPartie(tablemorpion)
        if (resultat == "X"):
            print("Le gagnant de la partie est joueur X")
        elif (resultat == "O"):
            print("Le gagnant de la partie est joueur O")
        elif (resultat == "null"):
            print("La partie de termine sur un match null")
        else:
            break
