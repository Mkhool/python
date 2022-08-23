nombre1 = 0
nombre2 = 0

while nombre1 == 0 and nombre2 == 0:
    nombre1_str = input("Veuillez entrer un premier nombre : ")
    nombre2_str = input("Veuillez entrer un deuxieme nombre : ")

    try:
        nombre1 = int(nombre1_str)
        nombre2 = int(nombre2_str)

    except ValueError:
        print("ERREUR: Vous devez rentrez un nombre pour l'age.")

nombre3 = int(nombre1_str) + int(nombre2_str)
print("l'addition de " + str(nombre1_str) + " et " + str(nombre2_str) + " est égal à " + str(nombre3))
