from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

from register import RegisterPage
from login import LoginPage

class MainCls:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome To My Bank")
        button_login = Button(self.root,text='Login',command=self.login)
        button_login.grid(row=1,column=1)
        button_register = Button(self.root,text='Register',command=self.register)
        button_register.grid(row=1,column=2)


    def login(self):
        self.root.withdraw()
        login_wind = Toplevel(self.root)
        LoginPage(login_wind)

    def register(self):
        self.root.withdraw()
        login_wind = Toplevel(self.root)
        RegisterPage(login_wind)

root = Tk()
MainCls(root)
root.mainloop()
