
#Créez une classe Animal avec un attribut age initialisé à zéro et prénom initialisé vide
#Instancier un objet Animal et écrire en console l’attribut âge. Créer une méthode “vieillir”qui ajoute 1 à l'âge de l’animal. Faire vieillir votre animal et afficher son âge en console.

class Animal :
    
    
    def __init__(self) :
        self.age = 0
        self.prenom = ""
    
    def vieillir(self) :
        self.age += 1

    def nommer(self) :
        self.prénom = "Luna"   

animal = Animal ()
print ("L'age de l'animal", animal.age)

animal.vieillir() 
print ("Le nouvel age de l'animal", animal.age)

animal.nommer()
print ("L'animal se nomme",animal.prénom )






