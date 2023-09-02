#Scope

#Scope Locale
def funzione():
    x = 300

    def sottoFunzione():
        print(x)
    sottoFunzione()

funzione()


#Scope Globale

y = 500

def glob():
    print(y)

glob()


#parole chiavi GLOBALI

def parola():
    global i   #KeyWord
    i = 100
    print(i)
parola()