#set
x = {"milano", "roma", "napoli"}
y = {"venezia", "udine"}

# possiamo solo aggiungere o rimuovere elementi
x.add("venezia")

x.update(y)
x.remove("milano")
x.discard("cagliari")

print(x)



#possiamo unire
u = {"italia", "america", "trento"}
l = {"palermo", "catania", "siracusa", "america"}

z = u.union(l)  #genera un nuovo set
u.update(l)     #aggiorna il set

#intersection
u.intersection_update(l)

print(u)