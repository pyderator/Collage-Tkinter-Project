from tkinter import *
from tkinter import messagebox
import con_to_sql as sql_conn
class ForgetPassword:

    """Security Questions"""
    security_questions = [{"id":1,"question":"What is your pet name?"},{"id":2,"question":"What is your first school name?"},{"id":3,"question":"What is your first love name?"}]

    def __init__(self,root, user=None):
        self.root = root
        self.root.title('Welcome To Bank')
        self.root.geometry('450x230')
        self.frame_login = Frame(self.root,height=300,width=300)
        self.frame_login.grid(row=0,column=0)
        self.user= user
        self.forgetpassword()
        self.root.resizable(0,0)


    def forgetpassword(self):
        """ Runs at first and checks if user exists and if yes fetches the question id"""
        def getData():
            username = input_username.get()

            # initiator of RecoverPassword, used as a reference all over

            self.initiated_data = sql_conn.RecoverPassword()
            returned_data = self.initiated_data.login(username)
            if returned_data:
                self.frame_login.destroy()
                self.forgetpassword_frame = Frame(self.root,height=300,width=300)
                self.forgetpassword_frame.pack()
                self.RecoverPassword(username,returned_data)
            else:
                messagebox.showerror('Error', 'User Doesnt Exits :(')

        login_text = Label(self.frame_login,text='Follow The Steps To Recover Your Account',font=('Nunito',16))
        login_text.pack(fill=X, padx=10, pady=5)

        input_username_text = Label(self.frame_login,text='Enter Your Username',font=('Nunito',16))
        input_username_text.pack(fill=X, padx=10, pady=2)
        input_username = Entry(self.frame_login, font=('Nunito', 15), justify='center')
        if self.user:
            input_username.insert('0',self.user)
        input_username.pack(fill=X, ipadx=5, padx=10, pady=10)

        button_login = Button(self.frame_login,text='Login',command=getData, font=('Nunito', 15))
        button_login.pack(fill=X, padx=10, pady=10)

    def RecoverPassword(self,username,returned_data):
        '''Runs after forgetpassword, makes a frame and checks the id associated
        with the question and searches it and then puts it in label'''
        self.root.geometry('700x230')

        help_text = Label(self.forgetpassword_frame,text=f"Welcome {username} Please Enter The Answer Of Your Security Question", font=('Nunito', 16))
        help_text.pack(fill=X, padx=10, pady=10)
        user_data = self.initiated_data.recoverpassword(returned_data)
        self.user_id = user_data[0]

        res = filter(lambda x: x.get('id') == user_data[0], ForgetPassword.security_questions)

        label_text = Label(self.forgetpassword_frame, text = next(res).get('question'), font=('Nunito', 16))
        label_text.pack(fill=X)

        label_entry = Entry(self.forgetpassword_frame, font=('Nunito', 15), justify='center')
        label_entry.pack(fill=X, pady=10, ipadx=3, padx=10)

        def trigger_password_reset():
            '''Check triggers the first stage of changing password'''

            if label_entry.get() == user_data[1]:
                self.forgetpassword_frame.destroy()
                self.changepassword(user_data[0])
            else:
                messagebox.showerror('Error','Answer is wrong')
        label_button = Button(self.forgetpassword_frame,text='Submit',command=trigger_password_reset, font=('Nunito',15))
        label_button.pack(fill=X, padx=10, pady=10)


    def changepassword(self,user_id):
        self.root.geometry('300x180')
        '''Asks the user for the new password and then triggers another function to change the password'''
        self.changepassword_frame = Frame(self.root,height=300,width=300)
        self.changepassword_frame.pack()
        label_text = Label(self.changepassword_frame,text='Enter Your New Password', font=('Nunito', 16))
        label_text.pack(fill=X, padx=10, pady=10)
        self.password_entry = Entry(self.changepassword_frame, font=("Nunito", 15), justify='center')
        self.password_entry.pack(fill=X, padx=10, pady=10, ipadx=3)
        button = Button(self.changepassword_frame,text='Change',command=self.changeit, font=('Nunito', 15))
        button.pack(fill=X, padx=10, pady=10)

    def changeit(self):
        '''Finally changes the password'''
        try:
            self.initiated_data.changepassword(self.password_entry.get())
        except Exception as e:
            messagebox.showerror('Error :( ', 'Something Went Wrong \n Please Try Again Later')
        else:
            messagebox.showinfo('Success :) ', 'Password Changed Successfully')
            self.root.withdraw()
