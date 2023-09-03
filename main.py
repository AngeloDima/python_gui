# DB
# pip install-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pysql"
)

cursor = db.cursor()

sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = ("Luca", "Rossi")
    

#executemany manda tanti dati  con execute manda un solo dato
cursor.execute(sql, values)
db.commit()

# dimmi l'ultimo id della table
print("id riga inserita: ", cursor.lastrowid)