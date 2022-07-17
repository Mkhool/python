from configparser import LegacyInterpolation
from random import randint
from re import I
import time

# creer class ricochet, donne un nombre de rebont
# lancer = decrementer le tir 
# ramasser = prendre une pierre

pierre = 0
player = False

class Ricochet():

    def __init__(self, pierre):

        self.pierre = pierre
        self.pierre = 1

    def ramasser (self, pierre):
        self.pierre += 1  
        print(f"vous avez {pierre} pierre.")

    def lancer(self):
        if self.pierre <= 0:
            print("vous n'avez plus de pierre à lancer, ramassez en une !")
            return
        self.pierre -= 1
        i = randint(0, 5)
        if i < 2:
            print(f" La pierre a fait {i} ricochet !")
        else:
            print(f" La pierre a fait {i} ricochets !")

while True:
    player = input("Voulez lancer une pierre ? yes or quit\n")
    if player == "yes":
        choix_player = input("vous pouvez soit 1. ramasser ou 2. lancer ue pierre\n")
        if choix_player == "ramasser":
                Ricochet.ramasser()
        else:
            print("vous devez faire un choix")
    elif player =="quit":
        time.sleep(3)
        break