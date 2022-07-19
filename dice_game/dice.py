from random import *

reponse = input("voulez vous jouer ? y/n     :")

if reponse == "n":
    print("dommage...")
elif reponse == "y":
    dice=input("allons y, choissisez votre dé: \n 1.d6 \n 2.d8 \n 3.d10 \n 4.d20 \n 5.d100 \n :     ")
    if dice == "1":
        roll = randint(1,6)
        print(roll)
    elif dice == "2":
        roll = randint(1,8)
        print(roll)
    elif dice == "3":
        roll = randint(1,10)
        print(roll)
    elif dice == "4":
        roll = randint(1,20)
        print(roll)
    elif dice == "5":
        roll = randint(1,100)
        print(roll)
    else:
        print("choissisez entre 1, 2, 3, 4, ou 5")
else:
    print("il faut choisir en tapant la lettre y ou n")
