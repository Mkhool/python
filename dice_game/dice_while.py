from random import *
from tkinter import Y
import sys

jouer=" "
new_game="yes"

def game():
    dice=input("\n Choissisez votre dé: \n 1.d6 \n 2.d8 \n 3.d10 \n 4.d20 \n 5.d100 \n :     ")
    if dice == "1":
            roll = randint(1,6)
            print("le résultat du lancé d6 est:",roll)
    elif dice == "2":
            roll = randint(1,8)
            print("le résultat du lancé d8 est:",roll)
    elif dice == "3":
            roll = randint(1,10)
            print("le résultat du lancé d10 est:",roll)
    elif dice == "4":
            roll = randint(1,20)
            print("le résultat du lancé d20 est:",roll)
    elif dice == "5":
            roll = randint(1,100)
            print("le résultat du lancé d100 est:",roll)
    else:
            print("choissisez entre les chiffres: 1, 2, 3, 4, ou 5")

jouer=input("voulez vous jouer ? yes/no     : \n")

if jouer == "no":
    print("dommage...")
    sys.exit()
elif jouer == "yes":
    print(game())
else:
    print("il faut choisir en ecrivant le mot yes ou no")

while new_game==input("voulez vous rejouer ? yes/no     : \n") == new_game =="yes" or new_game=="y":
    print(game())

