import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Instagram Bot by Carl")

Statistics = Label(window, text="Statistics")
Statistics.config(font=("Courier", 32))
Statistics.place(x=20, y=20)

Followers = Label(window, text="Followers")
Followers.config(font=("Courier", 32))
Followers.place(x=300, y=5)

Following = Label(window, text="Following")
Following.config(font=("Courier", 32))
Following.place(x=600, y=5)

Follow = Label(window, text="Follow")
Follow.config(font=("Courier", 32))
Follow.place(x=20, y= 150)

UnFollow = Label(window, text="UnFollow")
UnFollow.config(font=("Courier", 32))
UnFollow.place(x=20, y=250)

Grow = Label(window, text="Grow")
Grow.config(font=("Courier", 32))
Grow.place(x=20, y=350)

Engage = Label(window, text="Engage")
Engage.config(font=("Courier", 32))
Engage.place(x=20, y=450)




window.geometry("900x600")
window.mainloop()