class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


# Création d'un rectangle de longueur 10 et de largeur 5
        rectangle = Rectangle(10, 5)


# Affichage de la longueur et de la largeur du rectangle
        print("Longueur :", rectangle.get_longueur())
        print("Largeur :", rectangle.get_largeur())

# Modification de la longueur et de la largeur du rectangle
        rectangle.set_longueur(6)
        rectangle.set_largeur(3)

# Affichage de la longueur et de la largeur du rectangle après modification
        print("Longueur modifiée :", rectangle.get_longueur())
