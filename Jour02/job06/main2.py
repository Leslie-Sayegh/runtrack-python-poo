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


