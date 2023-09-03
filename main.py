# DB
# pip install-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pysql"
)

#INNER, LEFT, RIGHT JOIN

cursor = db.cursor()
sql = "SELECT \
    nome, cognome, citta.nome_citta \
    FROM clienti \
    INNER JOIN citta ON clienti.citta = citta.id"

cursor.execute(sql)
result = cursor.fetchall()
for riga in result:
    print(riga)
