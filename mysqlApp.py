import random
import tkinter
import tkinter as tk
import tkinter.messagebox

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


def insertNewRowIntoUserTable(username, password, repeatedPassword):

    if(len(username)==0):
      tkinter.messagebox.showinfo("Message", "Please enter a username!")
      return None

    if (len(password) < 6):
        tkinter.messagebox.showinfo("Message", "Please enter a password (at least 6 characters)!")
        return None

    if(password != repeatedPassword):
        tkinter.messagebox.showinfo("Message", "The passwords are not the same!")
        return None

    if(checkIfUsernameExists(username)):
        tkinter.messagebox.showinfo("Message", "This username already exists!")
        return None

    id = random.randint(0, 10000000)

    while (checkIfIdExists(id)):
        id = random.randint(0, 10000000)

    cursor.execute(
        "insert into user (id,username,password) VALUES ('" + str(id) + "','" + username + "','" + password + "')")
    database.commit()
    tkinter.messagebox.showinfo("Message", "Created new account successfully!")


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

def buildInsertNewRowGUI(window):
    window.destroy()
    mainWindow = tk.Tk()
    mainWindow.title("Registration")
    mainWindow.resizable(False,False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Username:")
    label1.pack()

    textinput1 = tk.Entry(mainWindow,width="50")
    textinput1.pack()

    label2 = tk.Label(mainWindow, text="Password:")
    label2.pack()

    textinput2 = tk.Entry(mainWindow,width="50")
    textinput2.pack()

    label3 = tk.Label(mainWindow, text="Repeat password:")
    label3.pack()

    textinput3 = tk.Entry(mainWindow,width="50")
    textinput3.pack()

    newUserButton = tk.Button(mainWindow, text="Create new account",
                              command=lambda: insertNewRowIntoUserTable(textinput1.get(),textinput2.get(),textinput3.get()))
    newUserButton.pack()

    resetButton = tk.Button(mainWindow,text="Reset"
                            , command=lambda: deleteInput(textinput1,textinput2,textinput3))
    resetButton.pack()

    loginButton = tk.Button(mainWindow, text="Login",
                              command=lambda: buildLoginGUI(mainWindow))
    loginButton.pack()

    deleteButton = tk.Button(mainWindow, text="Delete account",
                              command=lambda: buildDeleteGUI(mainWindow))

    deleteButton.pack()

    mainWindow.mainloop()

def deleteAccount(username,password):
    cursor.execute("select * from user where username='" + username + "' and password='" + password + "'")
    result = cursor.fetchall()
    if (len(result) == 0):
        tkinter.messagebox.showinfo("Message", "Wrong username/password!")
    else:
        tkinter.messagebox.showinfo("Message", "Delete request successful!")
        cursor.execute("delete from user where username='" + username + "' and password='" + password + "'")
        database.commit()

def buildDeleteGUI(window):
    window.destroy()
    mainWindow = tk.Tk()
    mainWindow.title("Delete account")
    mainWindow.resizable(False, False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Username:")
    label1.pack()

    textinput1 = tk.Entry(mainWindow, width="50")
    textinput1.pack()

    label2 = tk.Label(mainWindow, text="Password:")
    label2.pack()

    textinput2 = tk.Entry(mainWindow, width="50")
    textinput2.pack()

    deleteButton = tk.Button(mainWindow, text="Delete account",
                             command=lambda: deleteAccount(textinput1.get(),textinput2.get()))

    deleteButton.pack()

    loginButton = tk.Button(mainWindow, text="Login",
                            command=lambda: buildLoginGUI(mainWindow))
    loginButton.pack()

    createNewAccountButton = tk.Button(mainWindow, text="Create new account",
                                       command=lambda: buildInsertNewRowGUI(mainWindow))
    createNewAccountButton.pack()

    mainWindow.mainloop()



def deleteInput(textinput1,textinput2,textinput3):
    textinput1.delete(0, "end")
    textinput2.delete(0, "end")
    textinput3.delete(0, "end")

def buildLoginGUI(window):
    window.destroy()
    mainWindow = tk.Tk()
    mainWindow.title("Login")
    mainWindow.resizable(False, False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Username:")
    label1.pack()

    textinput1 = tk.Entry(mainWindow, width="50")
    textinput1.pack()

    label2 = tk.Label(mainWindow, text="Password:")
    label2.pack()

    textinput2 = tk.Entry(mainWindow, width="50")
    textinput2.pack()

    loginButton = tk.Button(mainWindow, text="Login",
                              command=lambda: login(textinput1.get(), textinput2.get()))
    loginButton.pack()

    createNewAccountButton = tk.Button(mainWindow, text="Create new account",
                            command=lambda: buildInsertNewRowGUI(mainWindow))
    createNewAccountButton.pack()

    deleteButton = tk.Button(mainWindow, text="Delete account",
                             command=lambda: buildDeleteGUI(mainWindow))

    deleteButton.pack()

    mainWindow.mainloop()

def login(username, password):
    cursor.execute("select * from user where username='"+username+"' and password='"+password+"'")
    result = cursor.fetchall()
    if(len(result)==0):
        tkinter.messagebox.showinfo("Message", "Wrong username/password!")
    else:
        tkinter.messagebox.showinfo("Message", "Login successful!")

window = tk.Tk()
buildInsertNewRowGUI(window)





