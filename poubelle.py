entree="rien"
n = 0
while entree != "":
    entree=input("Tapez un mot (ou juste 'Enter' pour quitter) : ")
    n += 1
    if entree != "":
        print(n,entree)
print("Au revoir !")