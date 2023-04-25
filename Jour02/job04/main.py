class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

forme = Forme()
print(forme.aire())  # Output: 0

rectangle = Rectangle(5, 3)
print(rectangle.aire())  # Output: 15
