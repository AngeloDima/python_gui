#Moduli
                # con as cambio nome al modulo
import mioModulo as em

#prendo solo un valore del modulo
x = em.persona1["nome"]
em.saluta(x)

#ciclo il modulo
for chiave, valore in em.persona1.items():
    print(f"{chiave}: {valore}")


#moduli built
import platform
a = platform.system()
print(a)



import math
print(math.floor(2.9))


#funzione dir MI DICE TUTTE LE FUNZIONI DI UN MODULO
print(dir(math))


#prendere solo una parte del modulo
from mioModulo import persona1
print(persona1["nome"])
