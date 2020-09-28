from tkinter import *
import os
from os import path

def CreateCreds():
    loc = os.getcwd()
    print(loc)
    if path.exists(loc + "\\creds.py"):
        os.remove("creds.py")
    

    with open(loc + "\\creds.py", 'w') as f:
        f.write("username = '{}'".format(uname_inp.get()))
        f.write("\n")
        f.write("pwd = '{}'".format(pwd_inp.get()))
        f.write("\n")

        path_text = ''
        for i in range(len(path_inp.get())):
            if path_inp.get()[i] == "\\": 
                path_text += "\\\\"
            else:
                path_text += path_inp.get()[i]
        
        f.write("Project_Location = '{}'".format(path_text))
    window.destroy()

window = Tk()

window.geometry("500x200")

window.wm_title("Set-Default-arguments")

l1 = Label(window, text = "Username/ Email: ", width=30, font=("Times New Roman", 14))
l1.grid(row = 1, column = 0, padx=0, pady=15)

uname_inp = StringVar()
t1 = Entry(window, textvariable=uname_inp)
t1.grid(row = 1, column = 1, padx=0, pady=15)

l2 = Label(window, text = "Password: ", width=30, font=("Times New Roman", 14))
l2.grid(row = 3, column = 0, padx=0, pady=15)

pwd_inp = StringVar()
t2 = Entry(window, textvariable=pwd_inp)
t2.grid(row = 3, column = 1, padx=0, pady=15)

l3 = Label(window, text = "Path to Projects Folder: ", width=30, font=("Times New Roman", 14))
l3.grid(row = 5, column = 0, padx=0, pady=15)

path_inp = StringVar()
t3 = Entry(window, textvariable=path_inp)
t3.grid(row = 5, column = 1, padx=0, pady=15)

b1 = Button(window, width=18, text = "Create Credentials",command=CreateCreds)
b1.grid(row = 7, column = 0, columnspan=2, rowspan = 2)
window.mainloop()
