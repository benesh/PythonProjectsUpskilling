# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


# from morpionGame.modele.modeleMorpion import MorpionTable,SessionGame,CreateSessionGame,Gamer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
class Myclass():
    i = 'canine'
    def __int__(self,name):
        self.name = name
    def f(self):
        return 'hello World'
    # def add(self,number):
    # -- self.i.append(number)


class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5
    tab = []

if __name__ == '__main__':
    """game = CreateSessionGame
    print(game.gamer1.nameGamer)
    game.pushInstancesAndStartGame"""

    new_shark = Shark()
    new_shark2 = Shark()
    #new_shark2.tab.append("Omar") => Shark.tab.append("Omar")
    new_shark2.tab = new_shark2.tab.append("Omar")
    new_shark2.animal_type = "Dog"

    print(new_shark.animal_type)
    print(new_shark.location)
    print(new_shark.followers)
    print(new_shark.tab)

    print(new_shark2.animal_type)
    print(new_shark2.location)
    print(new_shark2.followers)
    print(new_shark2.tab)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
