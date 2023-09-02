#Json

import json

x = '{"nome": "angelo", "cognome": "di mauro"}'
#da Json a python
y = json.loads(x)
print(y)



q = {
    "nome": "angelo",
    "cognome": "di mauro"
}
#da python a Json
a = json.dumps(q)
print(a)


#formattare un Json    INDED=valore  ,  SEPARATORS,    in ordine alfabetico   SORT_KEYS=TRUE

k = {
    "nome": "Angelo",
    "cognome": "di mauro",
    "citta": "Trento",
    "anni": 20,
    "passioni": ["palestra", "moto"],
    "fidanzato": False
}

l = json.dumps(k, indent=4, separators=(". ", "= "), sort_keys=True)
print(l)