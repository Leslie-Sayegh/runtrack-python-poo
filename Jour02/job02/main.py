class Personne:
    def __init__(self, age=14):
        self.age = age

    def bonjour(self):
        print("Bonjour")

    def afficherAge(self):
        print("j'ai", self.age, 'ans')



    def modifierAge(self, nouveauAge):
        self.age = nouveauAge
        print("L'âge de la personne a été modifié avec succès")

# Exemple d'utilisation
p1 = Personne() # Crée une personne avec l'âge par défaut (14)
p1.bonjour() # Affiche "Hello"
p1.afficherAge() # Affiche "L'âge de la personne est 14"
p1.modifierAge(20) # Modifie l'âge de la personne à 20
p1.afficherAge() # Affiche "L'âge de la personne est 20"

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

eleve1 = Eleve("15") # Crée un élève avec l'âge de 16 ans
eleve1.bonjour() # Affiche "Hello"
eleve1.afficherAge() # Affiche "J'ai 16 ans"
eleve1.allerEnCours() # Affiche "Je vais en cours"
eleve1.affichageAge() # Affiche "J'ai 16 ans"

class Professeur(Personne):
    def __init__(self, age=30, matiereEnseignee=""):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Commencer le cour.")

    def afficherMatiereEnseignee(self):
        print("Je suis professeur de", self.__matiereEnseignee)

    def setMatiereEnseignee(self, matiere):
        self.__matiereEnseignee = matiere

# Exemple d'utilisation
prof1 = Professeur(40, "mathématiques")
prof1.bonjour() # Affiche "Hello"
prof1.afficherAge() # Affiche "j'ai 40 ans"
#prof1.afficherMatiereEnseignee() # Affiche "Je suis professeur de mathématiques"
prof1.enseigner() # Affiche "Le cours va commencer."
