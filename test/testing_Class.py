# # class Movie():
# #     def __init__ (self, name, release, notation):
# #         self.name =name
# #         self.release = release
# #         self.notation = notation

from dataclasses import dataclass
from platform import release

@dataclass #dataclass permet d'eviter les redites quand on cree une class avec init et self
class Movie:
    name: str #si on veut une valeur par defaut il faut mettre ""
    release: int
    notation:int 

avatar = Movie("Avatar", "2001", "5")
saw = Movie("Saw", "2000", "3,5")

def afficher_info(self):
    print(f"Le film {self.name} est sorti en salle en {self.release} et a obtenu la note de {self.notation} sur 5 ")

afficher_info(avatar) 