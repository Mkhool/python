from asyncio.log import logger
from configparser import LegacyInterpolation
from email import message
import logging
from random import randint
from re import I
import time
import sys
# creer class ricochet, donne un nombre de rebont
# lancer = decrementer le tir 
# ramasser = prendre une pierre
logging.basicConfig(level=logging.WARNING,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime) - %(levelname)s - %(message)s')
pierre = 0
player = False

class Ricochet():

    def ramasser ():
        global pierre
        pierre += 1  


    def afficher_pierre():
        print(f"vous avez {pierre} pierre.\n")


    def lancer():
        global pierre
        i = randint(0, 5)

        if pierre <= 0:
            print("Vous n'avez plus de pierre à lancer, ramassez en une !")
        else:
            if i < 2:
                print(" La pierre a fait", i, "ricochet !" )
            else:
                print(" La pierre a fait", i, "ricochets !" )

        pierre -= 1
        if pierre <=0:
            print("Vous n'avez plus de pierre" "\n", 50* "-")
        else:
            print(" Il vous reste", pierre, "pierre" "\n", 50* "-")

player = input("Voulez jouer au jeu du ricochet ? yes or quit\n")

while True:
 
    if player == "yes":
        choix_player = input("Vous pouvez soit: \n1. Ramasser \n2. Lancer une pierre\n3. quit\nQuel est votre choix:\n")
        if choix_player == "1":
                Ricochet.ramasser()
                Ricochet.afficher_pierre()
        elif choix_player == "2":
                Ricochet.lancer()
        elif choix_player == "quit" or choix_player == "3":
            time.sleep(3)
            sys.exit("Bye Bye")
        else:
            print("vous devez faire un choix")
    elif player =="quit":
        time.sleep(3)
        sys.exit("Revenez quand vous voulez !")