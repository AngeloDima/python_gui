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

sql = "SELECT * FROM clienti ORDER BY nome LIMIT 4"
cursor.execute(sql)
result = cursor.fetchall()
for riga in result:
    print(riga)
