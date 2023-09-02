#Ereditarietà

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono " + self.nome)





#Eredita tutti metodi e i costruttori 
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia   #nuova proprietà che ha solo insegnate e non persona "PADRE"

    def saluta(self):
        print("buongiorno sono " + self.nome + ' ' + self.cognome)   #metodo ereditato però con l'overRide

    def voto(self):
        print("Bravo hai preso 10")



persona1 = Persona("Luca", "Rossi")
Insegnante1 = Insegnante("Anna", "Neri", "italiano")


persona1.saluta()
Insegnante1.voto()


print(Insegnante1.materia)