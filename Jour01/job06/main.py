#classe, ascenseur, mutateur

class Rectangle :

    def __init__(self, longueur, largeur) :
      self.longueur = longueur
      self.largeur = largeur
    def get_longueur(self) :
       return self.longueur
    
    def set_longueur(self, longueur) :
       self.longueur = longueur
    
    def get_largeur(self) :
       return self.largeur
    
    def set_largeur(self, largeur) :
       self.largeur = largeur

#création rectangle
mesure = Rectangle (10, 5)

#affichage mesure
print ("Longueur :", mesure.get_longueur())
print ("Largeur :", mesure.get_largeur())

#modification mesure
mesure.set_longueur(6)
mesure.set_largeur(3)

#affichage mesure modif
print("Longueur modifiée :", mesure.get_longueur())
print("Largeur modifiée :", mesure.get_largeur())




