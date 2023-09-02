#tuple

q  = tuple(("Milano", "Catania"))
w = ("Catania", True, 4)

print((q))

#Controllo se un elemento esiste dentro una tuple o lista
if "Catania" in q:
    print("OK")
else:
    print("non trovato")

print("------")
print("------")
print("------")
print("------")


#manipolare i diversi "contenitori" e trasformali a piacimento ESS...
#Le tuple non possono essere modificate le liste si
e = ("India", "Monaco", "Palermo")
r = list(e)
r[0] = "italia"
e = tuple(r)
print(r)


print("------")
print("------")
print("------")
print("------")

#spappolare una tupla in tante var
container = ("strappo", "slancio", "stacco", "panca", "panca")
(i,o,*p) = container
print(i)
print(o)
print(p)

#metodi
l = container.count("panca")
print(l)

l = container.index("panca")
print(l)