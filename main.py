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

sql = ("DROP TABLE IF EXISTS temporanea")
cursor.execute(sql)


