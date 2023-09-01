# Operatori logici AND,OR, NOT


x = 10


if x > 10 and x < 20:   #entrambe le condizioni sono verificate
    print("compreso tra 10 e 20")
else: 
    print("non verificato")




if x > 10 or x < 20:   #una delle due condizioni sono verificate e quindi va avanti
    print("compreso tra 10 e 20")
else: 
    print("non verificato")




if not(x < 10):   #va a negare la condizione e come il ! degli altri linguaggi
    print("compreso tra 10 e 20")
else: 
    print("non verificato")





if x > 10: print("Short End")   #Short, lo possiamo usare solo se c'è solo una istruzione dopo, SOLO UNA
                                #si puo usare anche il col elif e else



f = 3

if f % 2 == 0:
    if (f < 10):
        print("numero pari e minore di 10")
else:
    print("numero dispari, non mi interessa se è minore di 10 o meno")


