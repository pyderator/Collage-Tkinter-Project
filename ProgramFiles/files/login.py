from tkinter import *
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

        def getData():
            username = input_username.get()
            password = input_password.get()
            print(username,password)
            a = sql_conn.Login(username,password)

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
