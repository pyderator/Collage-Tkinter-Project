from tkinter import *
from tkinter import messagebox

# forget password

from forgetpassword import ForgetPassword
from acc_reg import RegisterAccount
class Dashboard:
    def __init__(self,root,username,user_id):

        self.root = root
        self.user = username
        self.user_id = user_id
        self.root.title(f'Dashboard, {self.user.upper()}')

        self.nav_frame = Frame(self.root,height=400,width=400)
        self.nav_frame.grid(row=0,column=1)

        self.nav_Home = Button(self.nav_frame,text='Home')
        self.nav_Home.grid(row=0,column=0)

        self.nav_register = Button(self.nav_frame,text='Register New Account',command=self.new_acc)
        self.nav_register.grid(row=0,column=1)

        self.nav_delete = Button(self.nav_frame,text='Delete Account')
        self.nav_delete.grid(row=0,column=2)

        self.nav_status = Button(self.nav_frame,text='Account Status')
        self.nav_status.grid(row=0,column=3)

        self.nav_changepw = Button(self.nav_frame,text='Change Password',command=self.changepassword)
        self.nav_changepw.grid(row=0,column=4)

        self.root.mainloop()


    def new_acc(self):
        accountregister = Toplevel(self.root)
        RegisterAccount(accountregister,self.user_id)

    def changepassword(self):
        change_pw = Toplevel(self.root)
        ForgetPassword(change_pw)
