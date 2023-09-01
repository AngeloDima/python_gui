# stringa normale
x = "ciao"


# Stringe multi riga
y = """ciao
        come
        va 
        io
        tutto
        bene"""

# prendimi l'indice della stringa x
print(len(x))


# ciclo for
for carattere in "computer":
    print(carattere)

# stampa fino al carattere ...
a = "ciao sono Angelo"
print(a[:4])

# stampa dal carattere ...
b = "ciao sono Angelo"
print(a[4:])

# stampa dentro quel range ...
o = "ciao sono Angelo"
print(a[4:8])


# indice negativo leva le ultime lettere 
u = "ciao python"
print(u[-2:])


# modificare una stringa
k = " ciao sono angelo "
print(k.upper())  #TUTTO GRANDE
print(k.lower())  #TUTTO PICCOLO
print(k.strip())  #LEVA LO SPAZZIO START - END
print(k.replace("o", "K"))  #RIMPIAZZA



#concatenare Stringe e numeri
c = 20
m = "ciao sono angelo e ho {} anni nato il {}"  #se specifici l'indice verrano ordinati come vuoi tu
print (m.format(c, 2002)) #se metti più valori verrano messi in ordine di scrittura



#Escape dei caratteri
h = "ciao sono angelo e voglio un \"gelato\""
print(h)
