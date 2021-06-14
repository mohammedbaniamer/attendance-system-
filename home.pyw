import tkinter as tk
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os 
import sys
from tkinter import ttk
import csv
import time
import datetime





def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "0" and password == "0"):

        messagebox.showinfo("","Login Success")
        log.destroy()
        main()
        

    else :
        messagebox.showinfo("","Incorrent Username and Password")
def treeview():
    os.system('python index.pyw')




def add():
    os.system('python "./system/trainPart.py"')




def ATT():
    os.system('python "./system/takingAttendancePart.py"')




def index():
    tree = Tk()
    tree.title("Python - Import CSV File To Tkinter Table")
    width = 500
    height = 400
    screen_width = tree.winfo_screenwidth()
    screen_height = tree.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    tree.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tree.resizable(0, 0)


    TableMargin = Frame(tree, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Num", "ID", "NAME"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Num', text="Num", anchor=W)
    tree.heading('ID', text="ID", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    ##########
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    filee = './system/all data\ ' + date + '\ Present Students.csv'
    with open(filee) as f:
    ##########
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            firstname = row['Time']
            lastname = row['Student No.']
            address = row['Name']
            tree.insert("", 0, values=(firstname, lastname, address))

    #============================INITIALIZATION==============================
    if __name__ == '__main__':
        tree.mainloop()





def main():
    window = tk.Tk()
    window.title("")
    window.geometry("1400x900")
    window.resizable(0,0)
    window.configure(background='#f9f9f9')

    helv36 = font.Font(family='Helvetica', size=36, weight=font.BOLD)
    helv24 = font.Font(family='Helvetica', size=20, weight=font.BOLD)

    #logo
    img = ImageTk.PhotoImage(Image.open("JUST-Logo-01.png"))
    display = Canvas(window, bg="white", height=30, width=100, bd=0, highlightthickness=0)
    display.create_image(0, 0, image=img, anchor=NW, tags="IMG")
    display.grid(row=0, column=0, sticky='news')


    #title
    title = tk.Label(window, text="Smart Attaendance System ", bg="#f9f9f9", font=helv36)
    title.grid(row=0, column=1, columnspan=3, sticky='news')

    #button1
    mark_attendance = tk.Button(window, text="Take Attendance", bg="#00c0ef", font=helv24,command=ATT)
    mark_attendance.grid(row=1, column=0, columnspan=2, sticky='news', padx=(20, 10), pady=(20, 10))

    #button2
    check_attendance = tk.Button(window, text="Check Attendance", bg="#f39c11", font=helv24, command= index)
    check_attendance.grid(row=1, column=2, columnspan=2, sticky='news', padx=(10, 20), pady=(20, 10))

    #button3
    add_new_student = tk.Button(window, text="Add New Student", bg="#01a157", font=helv24, command=add)
    add_new_student.grid(row=2, column=0, columnspan=2, sticky='news', padx=(20, 10), pady=(10, 20))

    #button4
    search_student = tk.Button(window, text="logout", bg="#d84a38", font=helv24,command=window.quit)
    search_student.grid(row=2, column=2, columnspan=2, sticky='news', padx=(10, 20), pady=(10, 20))





    Grid.rowconfigure(window, 0, weight=1)

    for x in range(3):
        Grid.rowconfigure(window, x, weight=1)

    for y in range(4):
        Grid.columnconfigure(window, y, weight=1)






def tree():
    os.system('python index.py')        














log = Tk()
log.title("Login")
log.geometry("300x200")
global e1
global e2
log.configure(background='#f9f9f9')
Label(log, text="UserName").place(x=20, y=10)
Label(log, text="Password").place(x=20, y=40)

e1 = Entry(log)
e1.place(x=140, y=10)

e2 = Entry(log)
e2.place(x=140, y=40)
e2.config(show="*")
helv36 = font.Font(family='Helvetica', size=10, weight=font.BOLD)
helv24 = font.Font(family='Helvetica', size=10, weight=font.BOLD)
Button(log, text="Login", command=lambda:[Ok()] , bg="#d84a38", font=helv24,height = 1, width = 13).place(x=10, y=100)
Button(log, text="logout", command=log.quit , bg="#d84a38", font=helv24,height = 1, width = 13).place(x=10, y=140)




mainloop()