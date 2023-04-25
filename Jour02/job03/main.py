class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur

# création d'un rectangle de longueur 5 et de largeur 3
mon_rectangle = Rectangle(8, 4)

# calcul du périmètre du rectangle
perimetre = mon_rectangle.perimetre()
print("Le périmètre du rectangle est :", perimetre)

# calcul de la surface du rectangle
surface = mon_rectangle.surface()
print("La surface du rectangle est :", surface)
