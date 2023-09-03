# DB
# pip install-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pysql"
)

# cursor = db.cursor()

# CREATE DATABASE
# SHOW DATABASES
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)


#CREARE UNA TABLE
# cursor = db.cursor()
# cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHARD (255))")



#VEDERE LE TABLE
# cursor = db.cursor()
# cursor.execute("SHOW TABLES")
# for x in cursor:
#     print(x)



