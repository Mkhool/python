class Movie():
    def __init__ (self, name, release, notation):
        self.name =name
        self.release = release
        self.notation = notation

avatar = Movie("Avatar", "2001", "5")
saw = Movie("Saw", "2000", "3,5")

# def afficher_info(self, name, release, notation ):
#    print(f"Le film {avatar.name} est sorti en salle en {avatar.release} et a obtenu la note de {avatar.notation} sur 5 ")


def afficher_info(self):
    print(f"Le film {self.name} est sorti en salle en {self.release} et a obtenu la note de {self.notation} sur 5 ")

afficher_info(saw) 