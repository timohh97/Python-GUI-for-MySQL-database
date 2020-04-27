import mysql.connector

database = mysql.connector.connect(host="localhost",user="root",passwd="",database="besucher")

cursor = database.cursor()

cursor.execute("select * from user")

for i in cursor:
    print(i)




