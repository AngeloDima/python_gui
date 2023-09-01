#ciclo for

lista_citta = ["Torino", "Augusta", "Napoli"]

for citta in lista_citta:
    print(citta)


#ciclo while
while len(lista_citta) > 2:
    print("cacca")
    break


for riga in range(6):
    for colonna in range(4):
        colonna += 1
        print("(" + str(riga) + ":" + str(colonna) + ")")
else:
    print("ho finito")