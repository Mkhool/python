
class Voiture:
    
    def __init__ (self, marque, vitesse, prix):
        self.vitesse = vitesse
        self.prix = prix
        self.marque = marque

    @classmethod
    def lamborghini(cls):
        return cls(marque="lamborghini", vitesse=250, prix=200000)
    
    @classmethod
    def porsche(cls):
        return cls(marque= "porsche", vitesse=200, prix=18000)
    
    def __str__(self):
        return f"Voiture de marque {self.marque} avec une vitesse de {self.vitesse} km/h pour un prix de {self.prix} euros."


class Moto(Voiture):
    def __init__(self, marque, vitesse, prix):
        super().__init__(marque, vitesse, prix)

    @classmethod
    def ducati(cls):
        return cls(marque="Ducati", vitesse=300, prix=100000)

    def __str__(self):
        return f"Moto de marque {self.marque} avec une vitesse de {self.vitesse} km/h pour un prix de {self.prix} euros."
    

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
affichage_porsche = str(porsche)
print(affichage_porsche)

ducati = Moto.ducati()
affichage_ducati = str(ducati)
print(affichage_ducati)

