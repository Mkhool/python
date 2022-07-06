import random
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
        break
    
