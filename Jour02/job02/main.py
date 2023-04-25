class Personne:
  def __init__(self, nom, age=15):
    self.nom = nom
    self.age = age

  def afficherAge(self):
     print("Age :", self.age)
          

  def bonjour(self):
    print("Bonjour, je m'appelle", self.nom)

class Eleve(Personne):
  def allerEnCours(self):
    print("Je vais en cours.")

class Professeur(Personne):
  def enseigner(self):
    print("Le cours commence.")

eleve = Eleve("Jean", 15)
eleve.bonjour()
eleve.allerEnCours()

professeur = Professeur("Mme Dupont", 40)
professeur.bonjour()
professeur.enseigner()
