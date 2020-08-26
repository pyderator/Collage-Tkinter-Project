from tkinter import *
from dashboard import Dashboard
from admininterface import AdminInt
from tkinter import messagebox
from forgetpassword import ForgetPassword
import con_to_sql as sql_conn

class LoginPage:
    def __init__(self,root):

        self.root = root
        root.title('Welcome To Bank')
        root.geometry('335x350')

        self.frame_login = Frame(root)
        self.frame_login.pack(fill=X)
        self.login()

    def login(self):
        '''Gets data and then checks if username and password are valid or not'''

        def getData(*args):
            self.username = input_username.get()
            self.password = input_password.get()
            haslogged = sql_conn.Login()
            haslogged.login(self.username,self.password)
            if haslogged.islogged:
                if haslogged.is_admin:
                    admin = Toplevel(self.root)
                    AdminInt(admin)
                else:
                    self.root.withdraw()
                    dashboard_root = Toplevel(self.root)
                    Dashboard(dashboard_root,self.username,haslogged.user_id)

        login_text = Label(self.frame_login,text='Please Enter The Credentials',font='Nunito 14')
        login_text.pack()

        line=Frame(self.frame_login,height=1,width=600,bg="grey")
        line.pack(fill=X)

        input_frame = Frame(self.frame_login)
        input_frame.pack(fill=X)

        input_username_text = Label(input_frame,text='Username',font='Nunito 14')
        input_username_text.grid(row=0,column=0,ipadx=10)
        input_username = Entry(input_frame, font=('Nunito', 13))
        input_username.insert(0,'pyderator')
        input_username.grid(row=0, column=1,ipadx=3, pady=10)

        input_password_text = Label(input_frame,text='Password',font=('Nunito',14))
        input_password_text.grid(row=1,column=0,ipadx=10)
        input_password = Entry(input_frame, font=('Nunito', 13))
        input_password.insert(0,'highway')
        input_password.grid(row=1,column=1,ipadx=3, pady=10)

        button_login = Button(self.root,text='Login',command=getData, font=('Nunito', 14))
        button_login.pack(fill=X, padx=10, pady=10)
        self.root.bind('<Return>',getData)

        frame2 = Frame(self.root, highlightbackground="black",   highlightthickness=1)
        frame2.pack(fill=X, padx=10, pady=1)
        already_label = Label(frame2, text="Don't Have An Account ?", font=('Nunito', 14))
        already_label.pack(fill=X, padx=(10,10))

        button_reg = Button(frame2,text='Register',command=self.registerAcc, font=('Nunito', 14))
        button_reg.pack(fill=X, padx=10, pady=2)

        forget_label = Label(frame2, text="Forget Your Password ?", font=('Nunito', 14))
        forget_label.pack(fill=X, padx=(10,10))

        button_forget = Button(frame2,text='Forget Password',command=self.forgetPw, font=('Nunito', 14))
        button_forget.pack(fill=X, padx=10, pady=2)


    def registerAcc(self):
        from register import RegisterPage
        reg_win = Toplevel(self.root)
        RegisterPage(reg_win)
        reg_win.mainloop()

    def forgetPw(self):
        pw_win = Toplevel(self.root)
        ForgetPassword(pw_win)
