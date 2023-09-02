# List

x = ["Milano", "Roma", "Napoli", "Augusta"]
y = ["ciao", 1231, True]
z = list(("cane", "gatto", "elefante"))

# len(), type(), list()
print(len(x))
print(type(x))
print(x)
print(z)

#lavorare con i range
k = ["fragola", "carota", "mandarino", "elefante"]
k[1:3] = ["Roma", "Inter"]

print(k)


#append     SI AGGIUNGE ALLA FINE
mm = ["ciao", "lollo"] 
mm.append("ola")

print(mm)


#insert     SI INSERISCE NEL INDICE SPECIFICATO E SPOSTA TUTTO IL RESTO
oi = ["prova", "della", "asd"]
oi.insert(1, "ciao")
print(oi)


#extend     E COME UN APPEND MA CON PIU DATI QUINDI CON DEGLI ARRAY(List)
kj = ["bergamo", "bologna", "Taormina"]
ca = ["Glovo", "deliveroo"]
kj.extend(ca)
print(kj)



#REMOVE  SPECIFICARE COSA VUOI ELIMINARE
jj = ["ciao", "come", "alla"]
jj.remove("ciao")
print(jj)


#POP  ELIMINA L'ULTIMO O SPECIFICA L'INDICI
jj = ["ciao", "come", "alla"]
jj.pop()
print(jj)


#DEL   NON HO CAPITO
jj = ["ciao", "come", "alla"]
del jj[1]
print(jj)


#CLEAR   CANCELLA TUTTO
jj = ["ciao", "come", "alla"]
jj.clear()
print(jj)




#CICLARE LOOP
jj = ["ciao", "come", "alla"]
for parola in jj:
    print(parola)



#con il range 
for i in range(len(jj)):
    print(jj[i])

#con il while
po = ["q", "w"]
i = 0
while i < len(po):
    print(po[i])
    i += 1


#unire insieme più liste
d = ["Genova", "Gela"]
r = ["Italia", "America"]
print(d + r)

#con il for
for info in r:
    d.append(info)
print(d)

#con extend
d.extend(r)
print(d)


