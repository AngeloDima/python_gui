#Try Except

x = 5

try:
    print(x)
except NameError:
    print("x non definita")
except TypeError:                   #Intervieni sui problemi puoi specificare e non l'errore
    print("numero e stringa")
else:                               #Se tutto va bene
    print("nessun problema")


#Creiamo noi un errore
i = -1
if i < 0:
    raise Exception("numero minore di zero")
print("ciao")