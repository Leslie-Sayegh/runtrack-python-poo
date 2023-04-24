# créerclasse Personne pour plusieur personnes 
class Personne :
    def SePresenter(self) : 
       print (self)
    def __init__(self, name) :
      self.name = name

    def show_infos(self) :
       print ("SePresenter")
       print ("Je suis", self.name)

personne1 = Personne("Leslie Sayegh")
personne2 = Personne("David Sayegh")
personne1.show_infos()
personne2.show_infos()


   