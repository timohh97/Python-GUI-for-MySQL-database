import random
import tkinter as tk

import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="", database="besucher")

cursor = database.cursor()


def getRowOfUserTable(i):
    cursor.execute("select * from user")
    result = cursor.fetchall()

    print(result[i])


def getColumnOfUserTable(columnName):
    cursor.execute("select " + columnName + " from user")
    result = cursor.fetchall()

    for i in result:
     print(i)

    return result


def deleteRowOfUserTable(i):
    cursor.execute("select * from user")
    result = cursor.fetchall()
    print("Deleted the row: " + str(result[i]))

    idOfRow = str(result[i][0])

    cursor.execute("delete from user where id='" + idOfRow + "'")

    database.commit()


def deleteAllRows():
    cursor.execute("delete from user")
    database.commit()


def insertNewRowIntoUserTable(username, password):
    id = random.randint(0, 10000000)

    while(checkIfIdExists(id)):
     id = random.randint(0, 10000000)

    if(checkIfUsernameExists(username)):
        print("This username already exists!")
        return None

    cursor.execute(
        "insert into user (id,username,password) VALUES ('" + str(id) + "','" + username + "','" + password + "')")
    database.commit()


def checkIfIdExists(id):
    idColumn = getColumnOfUserTable("id")

    for element in idColumn:
        for entry in element:
         if(entry==id):
            return True

    return False


def checkIfUsernameExists(username):
    usernameColumn = getColumnOfUserTable("username")

    for element in usernameColumn:
        for entry in element:
            if (entry == username):
                return True

    return False

def buildInsertNewRowGUI():
    mainWindow = tk.Tk()
    mainWindow.title("Insert a new row")
    mainWindow.resizable(False,False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Username:")
    label1.pack()

    textinput1 = tk.Entry(mainWindow)
    textinput1.pack()

    label2 = tk.Label(mainWindow, text="Password:")
    label2.pack()

    textinput1 = tk.Entry(mainWindow)
    textinput1.pack()

    label3 = tk.Label(mainWindow, text="Repeat password:")
    label3.pack()

    textinput1 = tk.Entry(mainWindow)
    textinput1.pack()

    newUserButton = tk.Button(mainWindow, text="Create new user")
    newUserButton.pack()


    mainWindow.mainloop()



buildInsertNewRowGUI()





