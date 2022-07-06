# Ce n'est sÃ»rement pas comme Ã§a que cela se passe dans Hearthstone
# mais cela satisfait les contraintes.

from random import randint

ok = False  # sera True si on tire autre chose qu'une commune
for x in range(5):
    if randint(1,100)==1:
        print("Légendaire",end=" ")
        ok = True
    elif randint(1,100)<=5:
        print("Epique",end=" ")
        ok = True
    elif randint(1,100)<=28:
        print("Rare",end=" ")
        ok = True
    else:
        print("Commun",end=" ")
        
if not ok :
    print("Paquet non valide : que des communes")
        