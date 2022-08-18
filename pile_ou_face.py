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


tirage = Counter(mylist)

listepile = print(f'Le coté PILE est tombé {tirage.get("cote_pile")} fois')
listeface = print(f'Le coté FACE est tombé {tirage.get("cote_face")} fois')


