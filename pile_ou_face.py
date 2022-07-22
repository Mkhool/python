from random import random
from collections import Counter
mylist = []
listepile = []
listeface = []

for i in range(100):
    if random() < 0.50:
        mylist.append("cote_face")
    else:
        mylist.append("cote_pile")




if "cote_pile" in mylist:
    listepile.append(mylist)
else:
    listeface.append(mylist)

print(Counter(mylist))


"""for x in mylist:
    if "cote_pile" in x:
        listepile.append(x)
    else:
        listeface.append(x)

print(f'le coté pile est tombé {(len(listepile))} fois')
print(f'le coté face est tombé {(len(listeface))} fois')"""