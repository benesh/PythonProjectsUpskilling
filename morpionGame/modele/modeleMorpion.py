class MorpionTable:
    def __init__(self):
        self.arryMorpion = [["", "", ""], ["", "", ""], ["", "", ""]]

    def updateCell(self, rowNum, colNum, element_to_insert):
        self.arryMorpion[rowNum][colNum] = element_to_insert
"""le faire nen 50 ligne de code"""

"""
Class of gamer
attribute
nameGamer : name of the gamer 
pawn : type pawn btw w just have two type of pawn
game : the instance of the current game 
"""


class Gamer:
    """Edit the code for the correct implementation for object to be passed through"""
    game = MorpionTable


    def __init__(self, namegamer: str, pawn: str, game: MorpionTable):
        self.nameGamer = namegamer
        self.pawn = pawn
        self.morpiongame = game

    """
    method allow a gamer to position a pawn on the table
    """
    def putYourPawn(self, row: int, column: int):
        self.morpiongame.updateCell(row, column, self.pawn)


"""
class that hold the session of game 
"""


class SessionGame(MorpionTable, Gamer):

    def __init__(self, morpion: MorpionTable, gamer1: Gamer, gamer2: Gamer):
        self.game1 = gamer1
        self.gamer2 = gamer2
        self.morpion = morpion

    def runSessionGame(self):
        compteur = 0
        while (compteur < 4):
            print(f"le gamer {self.gamer1.nameGamer}")
            row = input("Saisir la ligne : ")
            col = input("Saisir la colonne : ")
            self.gamer1.putYourPawn(row, col)
            self.morpion
            compteur += 1
        print("fin de la session")


class CreateSessionGame(MorpionTable, Gamer, SessionGame):
    def __init__(self):
        self.morpiongame = MorpionTable
        self.gamer1 = Gamer("Omar", "X", self.morpiongame)
        self.gamer2 = Gamer("Ben", "O", self.morpiongame)
        self.sessiongame = SessionGame(self.morpiongame, self.gamer1, self.gamer2)

    def pushInstancesAndStartGame(self):
        self.sessiongame.runSessionGame()
