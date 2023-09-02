persona = {
    "nome": "angelo"
}

operazioni = ("add", "edit", "delete")

def start():
    key = input("quale operazione vuoi eseguire?: ")
    if key == operazioni[0]:
        kp = input("inserisci la chiave e il paramentro con la , come spazio: ")
        add(kp.split(","))

    elif key == operazioni[1]:
        chiave = input("chiave da modificare: ")
        valore = input("valore da modificare: ")
        edit(chiave, valore)

    elif key == operazioni[2]:
        chiave = input("chiave da eliminare: ")
        delete(chiave)


def add(p):
    chiave = p[0]
    valore = p[1]
    persona[chiave] = valore
    print(persona)



def edit(chiave,valore):
    if chiave in persona:
        persona[chiave] = valore
        print(persona)
    else:
        print("chiave non trovata")


def delete(chiave):
    if chiave in persona:
        del persona[chiave]
        print(persona)

while True:
    start()    