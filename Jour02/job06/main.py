class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix, "euros")

# Création d'une instance de Vehicule
mon_vehicule = Vehicule("Peugeot", "208", 2019, 15000)

# Affichage des informations du véhicule
mon_vehicule.informationsVehicule()


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
ma_voiture.informationsVehicule()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roues)

ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
ma_moto.informationsVehicule()


