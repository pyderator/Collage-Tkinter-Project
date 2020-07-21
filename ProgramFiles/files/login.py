from tkinter import *
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
        def getData():
            try:
                self.username = input_username.get()
                self.password = input_password.get()
                try:
                    Connection()
                except:
                    messagebox.showerror("Error","No Response From Database")
                    return False
                sql_conn.Login(self.username,self.password)
            except:
                messagebox.showerror("Error","Username or Password is wrong")

        login_text = Label(self.frame_login,text='Welcome To The Bank \n Please sign in to continue',font='Nunito')
        login_text.grid(row=1,column=1)

        input_username_text = Label(self.frame_login,text='UserName',font='Nunito')
        input_username_text.grid(row=2,column=1)
        input_username = Entry(self.frame_login)
        input_username.grid(row=2,column=2)

        input_password_text = Label(self.frame_login,text='Password',font='Nunito')
        input_password_text.grid(row=3,column=1)
        input_password = Entry(self.frame_login)
        input_password.grid(row=3,column=2)

        button_login = Button(text='Login',command=getData)
        button_login.grid(row=4,column=1)



root = Tk()
LoginPage(root)
root.mainloop()
