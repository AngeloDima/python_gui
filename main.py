# funzioni

def faiLaPasta(pasta, sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + pasta)
    if sugo:
        print("prepara il sugo")

faiLaPasta(sugo = True, pasta ="Penne")


print("--------")
print("--------")
print("--------")


#Return
def fai_somma(num1, num2):
    somma = num1 + num2
    return somma

x = fai_somma(2, 3)
print(x)
