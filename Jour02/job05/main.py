class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.radius**2
   
cercle = Cercle(5)
forme = Forme()

print("Aire du cercle :", cercle.aire()) # Output : Aire du cercle : 78.5
print("Aire de la forme :", forme.aire()) # Output : Aire de la forme : 0
