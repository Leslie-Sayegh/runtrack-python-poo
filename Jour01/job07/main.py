class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages
#ascensseur 
    def get_titre(self):
        return self.titre

    def get_auteur(self):
        return self.auteur

    def get_nb_pages(self):
        return self.nb_pages

#mutateur
    def set_titre(self, titre):
        self.titre = titre

    def set_auteur(self, auteur):
        self.auteur = auteur

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0 :
            self.nb_pages = nb_pages
        else :
            print("Erreur : Le nombre de pages doit être un entier positif.")
   
   

livre = Livre ("Python", "Leslie", 55)

print ("Titre :",livre.get_titre())
print ("Auteur :",livre.get_auteur())
print ("Nombre de pages :",livre.get_nb_pages())



