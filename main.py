#User input
import sys
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 21
}

operazioni = ("aggiungere", "modificare", "eliminare", "stoppa")

def start():
    operazione = input("cosa vuoi fare? ")
    if operazione == operazioni[0]:
        param = input("Aggiungi chiave valore: separati da una virgola ")
        aggiungi(param.split(","))

    elif operazione == operazioni[1]:
        chiave = input("Inserisci la chiave da modificare: ")
        valore = input("Inserisci il valore da modificare: ")
        modifica(chiave, valore)

    elif operazione == operazioni[2]:
        chiave = input("inserisci la chiave della persona da eliminare: ")
        eliminare(chiave)
    

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave]=valore
    print(persona)


def modifica(chiave, valore):
    if chiave in persona:
        persona[chiave] = valore
        print(persona)
    else:
        print("chiave non trovata nella persona")


def eliminare(chiave):
    if chiave in persona:
        del persona[chiave]
        print(f"Chiave '{chiave}' eliminata dalla persona")
    else:
        print("Chiave non trovata nella persona")




while True:
    start()


