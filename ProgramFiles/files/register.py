from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import con_to_sql as sql_conn
from login import LoginPage

class RegisterPage:
    security_questions = [{"id":1,"question":"What is your pet name?"},{"id":2,"question":"What is your first school name?"},{"id":3,"question":"What is your first love name?"}]
    def __init__(self,root):
        self.root = root
        root.title('Welcome To Bank')
        root.geometry('450x650')
        self.frame_login = Frame(root)
        self.frame_login.pack(fill=X)
        self.root.resizable(0,0)
        self.register()

    def register(self):

        def getData():

            '''Gets data from entry and registers them'''
            first_name = input_first_name.get()
            last_name = input_last_name.get()
            username = input_username.get()
            password = input_password.get()
            address = input_address.get()
            contact = input_contact.get()
            age = input_age.get()
            self.question = dropdown_security_questions.get()
            question_answer = dropdown_entry.get()
            if first_name and last_name and username and password and age and address and contact and self.question and question_answer:
                try:
                    for i in RegisterPage.security_questions:
                        if i.get('question') == self.question:
                            question_id=i.get('id')
                    res = sql_conn.Register().register(first_name,last_name,username,password,age,address,contact,question_id,question_answer)
                    if res:
                        messagebox.showinfo('Success','Registered Successfully')

                        # Opens the window for login

                        self.root.withdraw()
                        login_wind = Toplevel(self.root)
                        LoginPage(login_wind)
                    else:
                        messagebox.showerror('Error','Something Went Wrong \n Please Try Again Later')
                except Exception as e:
                    messagebox.showerror(title="Error", message='Something went wrong please try again')
            else:
                messagebox.showerror('Error', 'All fields are required')


        register_text = Label(self.frame_login,text='Register Now',font=('Nunito', 20))
        register_text.pack(fill=X, padx=10, pady=10)

        entry_font = ('Nunito', 14)
        input_font = ('Nunito', 16)
        inputs_frame = Frame(self.frame_login)
        inputs_frame.pack(fill=X,padx=10,pady=10)
        input_first_name_text = Label(inputs_frame,text='First Name',font=input_font)
        input_first_name_text.grid(row=0, column=0, ipadx=10, pady=10)
        input_first_name = Entry(inputs_frame, font=entry_font)
        input_first_name.grid(row=0, column=1, ipadx=3, pady=10)

        input_last_name_text = Label(inputs_frame,text='Last Name',font=input_font)
        input_last_name_text.grid(row=1, column=0, ipadx=10)
        input_last_name = Entry(inputs_frame, font=entry_font)
        input_last_name.grid(row=1, column=1, ipadx=3, pady=10)

        input_username_text= Label(inputs_frame,text='Username',font=input_font)
        input_username_text.grid(row=2,column=0 ,ipadx=10, pady=10)
        input_username = Entry(inputs_frame, font=entry_font)
        input_username.grid(row=2,column=1, ipadx=3, pady=10)

        input_password_text = Label(inputs_frame,text='Password',font=input_font)
        input_password_text.grid(row=3, column=0, ipadx=10)
        input_password = Entry(inputs_frame, font=entry_font)
        input_password.grid(row=3,column=1, ipadx=3, pady=10)

        input_address_text = Label(inputs_frame,text='Address',font=input_font)
        input_address_text.grid(row=4, column=0, ipadx=10)
        input_address = Entry(inputs_frame,font=entry_font)
        input_address.grid(row=4,column=1 ,ipadx=3, pady=10)

        input_contact_text = Label(inputs_frame,text='Contact',font=input_font)
        input_contact_text.grid(row=5, column=0, ipadx=10)
        input_contact = Entry(inputs_frame, font=entry_font)
        input_contact.grid(row=5,column=1 ,ipadx=3, pady=10)

        input_age_text = Label(inputs_frame,text='Age',font=input_font)
        input_age_text.grid(row=6, column=0, ipadx=10)
        input_age = Entry(inputs_frame, font=entry_font)
        input_age.grid(row=6,column=1 ,ipadx=3, pady=10)

        security_question_label = Label(inputs_frame,text='Security question', font=input_font)
        security_question_label.grid(row=7,column=0, ipadx=3, pady=10)

        vars = map(lambda x: x,RegisterPage.security_questions)
        data = []
        for i in vars:
            data.append(i.get('question'))
        dropdown_security_questions = Combobox(inputs_frame,value=data,width='25',state='readonly')
        dropdown_security_questions.current(0)
        dropdown_security_questions.grid(row=7,column=1 ,ipadx=3, pady=10)
        dropdown_entry = Label(inputs_frame,text="Answer", font=input_font)
        dropdown_entry.grid(row=8, column=0, ipadx=10)
        dropdown_entry = Entry(inputs_frame, font=entry_font)
        dropdown_entry.grid(row=8,column=1 ,ipadx=3, pady=10)

        button_login = Button(self.root,text='Register',command=getData, font=input_font)
        button_login.pack(fill=X, padx=10, pady=10)
