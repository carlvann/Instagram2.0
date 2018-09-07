from tkinter import *
import tkinter

class LogIn:

    window = tkinter.Tk()
    window.title("Login")
    window.configure(background = "white")

    Label(window, text = "User Name").grid(row=0)
    Label(window, text = "Password").grid(row=1)

    e1 = Entry(window)
    e2 = Entry(window)

    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)

    login = Button(window, text = "Log In", command = "")
    forgot = Button(window, text = "Forgot Password")

    login.grid(row = 3, column = 0, sticky = "W", pady =  8)
    forgot.grid(row = 3, column = 1, sticky= "W", pady =  8)

    window.mainloop()
