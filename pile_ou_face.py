from collections import Counter
from random import random
from collections import Counter
mylist = []
<<<<<<< HEAD
<<<<<<< HEAD
=======
listepile = []
listeface = []
>>>>>>> e919697b035a9a1b4135e7d7cdddb5044bd20b5b
=======
>>>>>>> ecd4ad7f3367f4797a687b5d3ce64b40a414bb50

for i in range(100):
    if random() < 0.50:
        mylist.append("cote_face")
    else:
        mylist.append("cote_pile")

<<<<<<< HEAD
tirage = Counter(mylist)

listepile = print(f'Le coté PILE est tombé {tirage.get("cote_pile")} fois')
listeface = print(f'Le coté FACE est tombé {tirage.get("cote_face")} fois')


"""
for x in mylist:
=======


for i in Counter(mylist).items():
    print(i)


"""if "cote_pile" in mylist:
    listepile.append(mylist)
else:
    listeface.append(mylist)"""

"""for x in mylist:
>>>>>>> e919697b035a9a1b4135e7d7cdddb5044bd20b5b
    if "cote_pile" in x:
        listepile.append(x)
    else:
        listeface.append(x)

print(f'le coté pile est tombé {(len(listepile))} fois')
<<<<<<< HEAD
print(f'le coté face est tombé {(len(listeface))} fois')
"""

=======
print(f'le coté face est tombé {(len(listeface))} fois')"""
>>>>>>> e919697b035a9a1b4135e7d7cdddb5044bd20b5b
