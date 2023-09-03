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

sql = "UPDATE clienti SET nome = %s WHERE ID = %s"
valori = ("Giggio", 9)
cursor.execute(sql,valori)

db.commit()
print("righe modificate: ", cursor.rowcount)