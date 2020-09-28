from selenium import webdriver
from time import sleep 
import sys
import os
from creds import username, pwd, Project_Location
from tkinter import *


class Accessing_GitHub:
    def __init__(self, uname, password, location):
        self.username = uname
        self.passwd = password
        self.location = location

        self.driver = webdriver.Chrome('C:\\Users\\Sid\\Documents\\Python\\lib\\site-packages\\selenium\\webdriver\\remote\\chromedriver.exe')
        self.driver.get("https://github.com/login")
        sleep(2)
        

        self.driver.find_element_by_id("login_field")\
            .send_keys(uname)
        sleep(1)

        self.driver.find_element_by_id("password")\
            .send_keys(password)
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')\
            .click()
        sleep(3)
        
        self.CreateRepo(uname, location)

    def CreateRepo(self, u, location):
        Rname = name_inp.get()
        description = description_inp.get()
        FileName = File_name_inp.get()
        self.driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')\
            .click()
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="repository_name"]')\
            .send_keys(Rname)
        sleep(1)

        if description != "/":
            self.driver.find_element_by_xpath('//*[@id="repository_description"]')\
                .send_keys(description)
            sleep(1)
        
        self.driver.find_element_by_xpath('//*[@id="repository_auto_init"]')\
            .click()
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')\
            .click()
        sleep(2)

        repoLink = "https://github.com/" + self.username + "/" + Rname + ".git"  

        os.chdir(location)
        print(os.getcwd())

        os.system("git clone " + repoLink)
        
        os.chdir(location + "\\\\" + Rname)
        print(os.getcwd())
        os.system("code " + FileName)
    
def Repo():
    u = username
    p = pwd
    project_path = Project_Location
    Accessing_GitHub(u, p, project_path)

window = Tk()

window.geometry("570x280")

l1 = Label(window, text = "Name of the Repository: ", width=30, font=("Times New Roman", 14))
l1.grid(row = 1, column = 0, padx= 0, pady=25)

name_inp = StringVar()
t1 = Entry(window, textvariable=name_inp)
t1.grid(row = 1, column = 1, padx=0, pady=25)

l2 = Label(window, text = "Description(use '/' for none): ", width=30, font=("Times New Roman", 14))
l2.grid(row = 5, column = 0, padx=0, pady=25)

description_inp = StringVar()
t2 = Entry(window, textvariable=description_inp)
t2.grid(row = 5, column = 1, padx=0, pady=25, columnspan=3)

l3 = Label(window, text = "Name of the file to be created (with extensions, e.g .py): ", font=("Times New Roman", 14))
l3.grid(row = 3, column = 0, rowspan=2, columnspan=3)

File_name_inp = StringVar()
t3 = Entry(window, textvariable=File_name_inp)
t3.grid(row = 3, column = 3, padx=0, pady=15, columnspan=2)

b1 = Button(window, width=18, text = "Initialize Repo",command=Repo)
b1.grid(row = 7, column = 0, columnspan=3, rowspan = 2)
window.mainloop()
