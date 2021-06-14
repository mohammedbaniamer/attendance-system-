from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os 
import sys
from tkinter import ttk
from home import *






def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "0" and password == "0"):

        messagebox.showinfo("","Login Success")
        log.destroy()
        

    else :
        messagebox.showinfo("","Incorrent Username and Password")



Ok()
        