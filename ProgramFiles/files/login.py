from tkinter import *
from dashboard import Dashboard
from admininterface import AdminInt
from tkinter import messagebox
try:
    from . import con_to_sql as sql_conn
except:
    import con_to_sql as sql_conn
class LoginPage:
    def __init__(self,root):

        self.root = root
        root.title('Welcome To Bank')
        root.geometry('500x500')

        self.frame_login = Frame(root,height=300,width=300)
        self.frame_login.grid(row=0,column=0)
        self.login()

    def login(self):
        '''Gets data and then checks if username and password are valid or not'''
        def getData(*args):

            self.username = input_username.get()
            self.password = input_password.get()
            haslogged = sql_conn.Login(self.username,self.password)
            if haslogged.islogged:
                # if haslogged.isadmin:
                #     admin = Toplevel(self.root)
                #     AdminInt(admin)
                # else:
                self.root.withdraw()
                dashboard_root = Toplevel(self.root)
                Dashboard(dashboard_root,self.username,haslogged.user_id)

        login_text = Label(self.frame_login,text='Welcome To The Bank \n Please sign in to continue',font='Nunito')
        login_text.grid(row=1,column=1)

        input_username_text = Label(self.frame_login,text='UserName',font='Nunito')
        input_username_text.grid(row=2,column=1)
        input_username = Entry(self.frame_login)
        input_username.insert(0,'oscar')
        input_username.grid(row=2,column=2)

        input_password_text = Label(self.frame_login,text='Password',font='Nunito')
        input_password_text.grid(row=3,column=1)
        input_password = Entry(self.frame_login)
        input_password.insert(0,'mike')
        input_password.grid(row=3,column=2)

        button_login = Button(self.root,text='Login',command=getData)
        button_login.grid(row=4,column=1)
        self.root.bind('<Return>',getData)
        print()
