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

sql = "SELECT * FROM clienti WHERE nome = 'Luca'"
cursor.execute(sql)
#prendo tutte le righe
result = cursor.fetchall()
for riga in result:
    print(riga)


#prendo solo una riga
# result = cursor.fetchone()
# print(result)
