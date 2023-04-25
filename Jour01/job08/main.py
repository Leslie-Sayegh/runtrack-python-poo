class Livre:

    #def __init__(self):
        #self.disponible = True   

    def __init__(self, titre, auteur) :
        self.titre = titre
        self.auteur = auteur
        #self.nb_pages = nb_pages
        self.disponible = True
    def vérification(self) :
        return self.disponible

    def disponible(self) :
        return self.disponible
  
    def disponible(self, value) :
        self.disponible = value

livre = Livre (6)
livre.disponible ()
print (livre)

#ascensseur 
    #def get_titre(self):
     #   return self.titre

    #def get_auteur(self):
     #   return self.auteur

    #def get_nb_pages(self):
     #   return self.nb_pages
    #def get_disponible(self):
     #   return self._disponible

#mutateur
    #def set_titre(self, titre):
        #self.titre = titre

    #def set_auteur(self, auteur):
        #self.auteur = auteur

    #def set_nb_pages(self, nb_pages):
        #self.nb_pages = nb_pages

    #def set_disponible(self, disponible):
        #self._disponible = disponible

#livre = Livre ("Python", "Leslie", 55)

#print ("Titre :",livre.get_titre())
#print ("Auteur :",livre.get_auteur())
#print ("Nombre de pages :",livre.get_nb_pages())



