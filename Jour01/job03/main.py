# ajouter méthode addition
class Opération :
 
    def __init__(self, nombre1, nombre2) :

        self.nombre1 = nombre1
        self.nombre2 = nombre2


    def show_Infos(self) :
        print ("Nombre1 :", self.nombre1)
        print ("Nombre2 :", self.nombre2)

    def add (nombre1, nombre2):
        adition=(nombre1 + nombre2)
        print("Résultat= ",adition)

    add (12, 3)

opération = Opération(12, 3)
        
opération.show_Infos()

print(opération)


