#dictionary

    # get(), keys(), values(), item()

persona = {
    "nome": "angelo",
    "cognome": "di mauro",
    "eta": 20,
    #si possono avere dict dentro i dict come se fosse un normale JSON
    "indirizzo": {
        "città": "augusta"
    }
}
print(persona["indirizzo"]["città"])


#modificare elementi con [] e update
persona["nome"] = "Marco"
persona.update({"nome": "anna"})

#aggiungere elementi con [] e update
persona["colore"] = "verde"
persona.update({"colore": "giallo"})

#rimuovere elementi con pop(), popitem(), clear(), del()

persona.pop("nome")
persona.clear()
del persona


#ciclare
for x in persona:   #oppure mettere dopo persona .values(), keys() ecc quello che vogliamo prendere
    print(persona[x])



print(persona)


#copiare   copy()

x = persona.copy()
print(x)

