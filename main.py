#Gestione dei file
# r = leggi, errore se non esiste
# a = append, crea se non esiste
# w = scrivi, crea se non esiste
# x = crea file, errore se siste

f = open("testo.txt", "r")


#leggi tutto o imposta un limite di caratteri READ
#leggi tutta la riga READLINE

print(f.read())

#per chiudere il file
f.close()



#Scrivo dentro un file esistente
f = open("testo.txt", "a")
f.write("CIAOOOOOOOOOOOOOOOOOOOO")
f.close()

#lo vado a leggere
f = open("testo.txt", "r")
print(f.read())
f.close()

#creo un file e ci vado a scrivere qualcosa
x = open("altro.txt", "w")
x.write("OLAOLAOLA")
x.close()


#elimino un file o una cartella
import os
os.remove("testo.txt")


#elimino un file o una cartella con una verifica
if os.path.exists("altro.txt"):
    os.remove("altro.txt")
else:
    print("questo file non esiste")


#elimina una cartella
os.rmdir("a")