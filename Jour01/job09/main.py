class Student:
    def init(self, nom, prenom, num_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.credits = 0
        self.level = self.student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits
            self.level = self.student_eval()

    def student_eval(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Identifiant : {self.num_etudiant}")
        print(f"Niveau : {self.level}")

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_total_credits(self):
        return self.credits

john_doe = Student("Doe", "John", 145)
john_doe.add_credits(30)
john_doe.student_info()

print(f"Le nombre de crédit de {john_doe.get_nom()} {john_doe.get_prenom()} est de {john_doe.get_total_credits()}")