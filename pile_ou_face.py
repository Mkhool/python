from collections import Counter
from random import random
mylist = []

for i in range(100):
    if random() < 0.50:
        mylist.append("cote_face")
    else:
        mylist.append("cote_pile")

tirage = Counter(mylist)

listepile = print(f'Le coté PILE est tombé {tirage.get("cote_pile")} fois')
listeface = print(f'Le coté FACE est tombé {tirage.get("cote_face")} fois')


"""
for x in mylist:
    if "cote_pile" in x:
        listepile.append(x)
    else:
        listeface.append(x)

print(f'le coté pile est tombé {(len(listepile))} fois')
print(f'le coté face est tombé {(len(listeface))} fois')
"""

