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

sql = "DELETE FROM clienti WHERE nome = %s AND cognome = %s"
valore = ("Paolo", "Gialli")
cursor.execute(sql, valore)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)


