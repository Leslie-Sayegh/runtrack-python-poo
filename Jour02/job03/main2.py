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
        
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
# création d'un rectangle de longueur 5 et de largeur 3
mon_rectangle = Rectangle(8, 4)

# accès à la longueur du rectangle
longueur = mon_rectangle.get_longueur()
print("La longueur du rectangle est :", longueur)

# modification de la longueur du rectangle
mon_rectangle.set_longueur(10)

# accès à la largeur du rectangle
largeur = mon_rectangle.get_largeur()
print("La largeur du rectangle est :", largeur)

# modification de la largeur du rectangle
mon_rectangle.set_largeur(6)

# calcul du périmètre du rectangle
perimetre = mon_rectangle.perimetre()
print("Le périmètre du rectangle est :", perimetre)

# calcul de la surface du rectangle
surface = mon_rectangle.surface()
print("La surface du rectangle est :", surface)

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

# création d'un parallélépipède de longueur 5, de largeur 3 et de hauteur 4
mon_parallelepipede = Parallelepipede(5, 3, 4)

# accès à la longueur du parallélépipède (hérité de la classe Rectangle)
longueur = mon_parallelepipede.get_longueur()
print("La longueur du parallélépipède est :", longueur)

# modification de la longueur du parallélépipède (hérité de la classe Rectangle)
mon_parallelepipede.set_longueur(6)

# accès à la hauteur du parallélépipède (défini dans la classe Parallelepipede)
hauteur = mon_parallelepipede.get_hauteur()
print("La hauteur du parallélépipède est :", hauteur)

# modification de la hauteur du parallélépipède (défini dans la classe Parallelepipede)
mon_parallelepipede.set_hauteur(5)

# calcul du volume du parallélépipède
volume = mon_parallelepipede.volume()
print("Le volume du parallélépipède est :", volume)
