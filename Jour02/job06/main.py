class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque : ", self.marque)
        print("Modèle : ", self.modele)
        print("Année : ", self.annee)
        print("Prix : ", self.prix)

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes : ", self.portes)

# Création d'un objet de la classe "Vehicule"
vehicule1 = Vehicule("Peugeot", "308", 2022, 25000)

# Affichage des informations du véhicule
vehicule1.informationsVehicule()

# Création d'un objet de la classe "Voiture"
voiture1 = Voiture("Renault", "Clio", 2023, 18000)

# Affichage des informations de la voiture
voiture1.informationsVehicule()

Marque :  Peugeot
Modèle :  308
Année :  2022
Prix :  25000
Marque :  Renault
Modèle :  Clio
Année :  2023
Prix :  18000
Nombre de portes :  4
