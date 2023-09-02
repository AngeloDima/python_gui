# Classi e oggetti
class Persona:
    #Costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    #metodo
    def saluta(self):
        print("ciao sono " + self.nome)

#instanzio una classe "PERSONA"
persona1 = Persona ("angelo", "Di mauro")
persona2 = Persona ("Maria", "Carla")


#richiamo il metodo
persona1.saluta()

#Cambio il nome di Persona2
persona2.nome = "Prati"
persona2.saluta()


#Eliminare un oggetto

del persona2.nome   #cancello solo un parametro
del persona2        #cancello tutto l'oggetto