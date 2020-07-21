from tkinter import *
from tkinter import messagebox
import con_to_sql as sql_conn
class ForgetPassword:

    """Security Questions"""
    security_questions = [{"id":1,"question":"What is your pet name?"},{"id":2,"question":"What is your first school name?"},{"id":3,"question":"What is your first love name?"}]

    def __init__(self,root):
        self.root = root
        root.title('Welcome To Bank')
        root.geometry('500x500')

        self.frame_login = Frame(root,height=300,width=300)
        self.frame_login.grid(row=0,column=0)
        self.forgetpassword()


    def forgetpassword(self):
        """ Runs at first and checks if user exists and if yes fetches the question id"""
        def getData():
            username = input_username.get()
            # initiator of RecoverPassword, used as a reference all over
            self.initiated_data = sql_conn.RecoverPassword()
            returned_data = self.initiated_data.login(username)
            if returned_data:
                self.frame_login.destroy()
                self.forgetpassword_frame = Frame(root,height=300,width=300)
                self.forgetpassword_frame.pack()
                self.RecoverPassword(username,returned_data)

        login_text = Label(self.frame_login,text='Follow The Steps To Recover Your Account',font='Nunito')
        login_text.grid(row=1,column=1)

        input_username_text = Label(self.frame_login,text='Enter Your Username',font='Nunito')
        input_username_text.grid(row=2,column=1)
        input_username = Entry(self.frame_login)
        input_username.grid(row=3,column=1)

        button_login = Button(self.frame_login,text='Login',command=getData)
        button_login.grid(row=4,column=0)

    def RecoverPassword(self,username,returned_data):
        '''Runs after forgetpassword, makes a frame and checks the id associated
        with the question and searches it and then puts it in label'''
        help_text = Label(self.forgetpassword_frame,text=f"Welcome {username} Please Enter The Answer Of Your Security Question")
        help_text.grid(row=0,column=0)
        user_data = self.initiated_data.recoverpassword(returned_data)
        print('the user id is',user_data)
        self.user_id = user_data[0]
        for i in ForgetPassword.security_questions:
            if i.get('id') == user_data[0]:
                label_text = Label(self.forgetpassword_frame,text=i.get("question"))
                label_text.grid(row=1,column=0)
        label_entry = Entry(self.forgetpassword_frame)
        label_entry.grid(row=2,column=0)

        def trigger_password_reset():
            '''Check triggers the first stage of changing password'''
            if label_entry.get() == user_data[1]:
                self.forgetpassword_frame.destroy()
                self.changepassword(user_data[0])
            else:
                messagebox.showerror('Error','Answer is wrong')
        label_button = Button(self.forgetpassword_frame,text='Submit',command=trigger_password_reset)
        label_button.grid(row=3,column=0)


    def changepassword(self,user_id):
        '''Asks the user for the new password and then triggers another function to change the password'''
        self.changepassword_frame = Frame(root,height=300,width=300)
        self.changepassword_frame.pack()
        label_text = Label(self.changepassword_frame,text='Enter Your New Password')
        label_text.grid(column=0,row=0)
        self.password_entry = Entry(self.changepassword_frame)
        self.password_entry.grid(column=1,row=0)
        button = Button(self.changepassword_frame,text='Change!!',command=self.changeit)
        button.grid(column=2,row=0)

    def changeit(self):
        '''Finally changes the password'''
        print("NEW Password",self.password_entry.get())
        self.initiated_data.changepassword(self.password_entry.get())

root = Tk()
ForgetPassword(root)
root.mainloop()
