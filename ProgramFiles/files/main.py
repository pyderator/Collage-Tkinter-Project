from tkinter import *
from tkinter import messagebox

from register import RegisterPage
from login import LoginPage


class MainCls:

    def __init__(self,root):

        self.root = root
        self.root.title("Welcome")
        self.root.geometry('600x260')
        self.root.resizable(0,0)

        show_label = Label(self.root, text='Welcome To The Maze Bank \nPlease Sign In or Register To Continue',font='Raleway, 19')
        show_label.pack(fill=X, padx=10, pady=20)

        button_frame = Frame(self.root, height=80, width=600)
        button_frame.pack(fill=X)
        button_login = Button(button_frame,text='Login',command=self.login,font='Nunito 17',width=18)
        button_login.place(relx=0.01,rely=0.2)
        button_register = Button(button_frame,text='Register',command=self.register,font='Nunito 17',width=18)
        button_register.place(relx=0.52,rely=0.2)


        line=Frame(self.root,height=1,width=600,bg="grey")
        line.pack(fill=X, pady=(4,0))

        show_details = Label(self.root, text='For More Info  \n  Tel Number: +977 522369, Mob Number: 999988888 \n Email: bank@bankmail.com', font='16')
        show_details.pack(fill=X, pady=2)


    def login(self):

        login_wind = Toplevel(self.root)
        LoginPage(login_wind)

    def register(self):

        login_wind = Toplevel(self.root)
        RegisterPage(login_wind)

root = Tk()
MainCls(root)
root.mainloop()
