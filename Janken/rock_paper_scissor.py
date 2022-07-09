import random
import time
# from tkinter import *
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper, or Scissors? or end to quit\n" ).capitalize()
    if computer == player:
        print("it's a tie!")
    elif player =="Rock":
        if computer=="Paper":
            print("You lose")
            cpu_score+=1
        else:
            print("you win")
            player_score+=1
    elif player =="Paper":
        if computer=="Scissors":
            print("you lose")
            cpu_score+=1
        else:
            print("you win")
            player_score+=1
    elif player =="Scissors":
        if computer=="Rock":
            print("you lose")
            cpu_score+=1
        else:
            print("you win")
            player_score+=1
    elif player=="End":
        print ("Final score:")
        print(f"score player {player_score}")
        print(f"score cpu {cpu_score}")
        if player_score == cpu_score:
            print("It's a tie!")
        elif player_score < cpu_score:
            print(".............You lose the game.............")
        else:
            print(".............You win the game.............")
        time.sleep(3)
        break
    


# #fenetre graphique
# fenetre= Tk()
# fenetre.title("Rock", "Paper", "Scissors")

# #images
# rien = PhotoImage(file="rien.gif")
# versus = PhotoImage(file="versus.gif")
# pierre = PhotoImage(file="pierre.gif")
# papier = PhotoImage(file="papier.gif")
# ciseaux = PhotoImage(file="ciseaux.gif")

# #labels
# texte1 = Label(fenetre, text="Humain:", font=("Helvetica", 16))
# texte1.grid(row=0, column=0)

# texte2 = Label(fenetre, text="Machine:", font=("Helvetica", 16))
# texte1.grid(row=0, column=2)

# texte3 = Label(fenetre, text="Pour jouez, cliquez sur une des icones ci-dessous.")
# texte1.grid(row=3, columnspan=3, pady=5)

# score1 = Label(fenetre, text="0", font=("Helvetica", 16))
# score1.grid(row=1, column=0)
# score2 = Label(fenetre, text="0", font=("Helvetica", 16))
# score2.grid(row=1, column=2)

# lab1 = Label(fenetre, image=rien)
# lab1.grid(row=2, column=0)
# lab2 = Label(fenetre, image=versus)
# lab2.grid(row=2, column=1)
# lab3 = Label(fenetre, image=rien)
# lab3.grid(row=2, column=2)

# #boutons
# bouton1 = Button(fenetre,command=jouer_pierre)
# bouton1.configure(image=pierre)
# bouton1.grid(row=4, column=0)
# bouton2 = Button(fenetre,command=jouer_papier)
# bouton2.configure(image=papier)
# bouton2.grid(row=4, column=1)
# bouton3 = Button(fenetre,command=jouer_ciseaux)
# bouton3.configure(image=ciseaux)
# bouton3.grid(row=4, column=2)
# bouton4 = Button(fenetre,text='Recommencer',command=reinit)
# bouton4.grid(row=5, column=0, pady=10, sticky=E)
# bouton5 = Button(fenetre,text='Quitter',command=fenetre.destroy)
# bouton5.grid(row=5, column=2, pady=10, sticky=W)

# # demarrage :
# fenetre.mainloop() 