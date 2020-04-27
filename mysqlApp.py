import mysql.connector

database = mysql.connector.connect(host="localhost",user="root",passwd="",database="besucher")

cursor = database.cursor()


def getRowOfUserTable(row):
    cursor.execute("select * from user")
    result= cursor.fetchall()

    print(result[row])


def getColumnOfUserTable(columnName):
    cursor.execute("select "+columnName+" from user")

    for i in cursor:
        print(i)

getColumnOfUserTable("username")



