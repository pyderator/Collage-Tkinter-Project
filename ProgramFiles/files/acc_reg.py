from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import con_to_sql as sql_conn

class RegisterAccount:
    def __init__(self,root,user_id):
        self.root = root
        root.title('Register New Account')
        self.frame_login = Frame(root)
        self.frame_login.pack(fill=X)
        self.user_id = user_id
        self.register()

    def register(self):

        def getData():
            '''Gets data from entry and registers them'''
            firstname = input_first_name.get()
            lastname = input_last_name.get()
            fathersname = input_fathersname.get()
            mothersname = input_mothersname.get()
            age = input_age.get()
            citizenshipnumber = input_citizenshipnumber.get()
            location = input_address.get()
            contact = input_contact.get()
            education = input_education.get()
            work = input_work.get()

            if firstname and lastname and fathersname and mothersname and age and citizenshipnumber and location and contact and education or work:
                register = sql_conn.AccRegAdmin(self.user_id,firstname,lastname,fathersname,mothersname,age,citizenshipnumber,location,contact,education,work)
                if register.isregistered:
                    messagebox.showinfo('Congrats','Successfully Registered')
                else:
                    messagebox.showerror('Error','Please Check Your Input And Contact The Bank Admin')
            else:
                messagebox.showerror('Error','Please Input All')


        register_text = Label(self.frame_login,text='Register New Bank Account',font=('Poppins',20))
        register_text.pack()
        dummy_text = '''

        Inorder to have a account, please fill the following:

        Rules:

        1. Do not hide your identity

        2. Your account will be checked and in response to that you may have
           or not your account. To check that please go to the pending account option

        3. If everything is valid, your bank account will be created with no initial money.
        '''
        register_req_text = Label(self.frame_login, text=dummy_text, font=('Poppins',15), justify='left')
        register_req_text.pack(fill=X)

        input_frame = Frame(self.frame_login)
        input_frame.pack(fill=X)

        input_first_name_text = Label(input_frame,text='First Name',font='Nunito 20')
        input_first_name_text.grid(row=0,column=0, padx=10, pady=0)
        input_first_name = Entry(input_frame, font='Nunito 18')
        input_first_name.grid(row=0,column=1, padx=10, pady=10)

        input_last_name_text = Label(input_frame,text='Last Name',font='Nunito 20')
        input_last_name_text.grid(row=0,column=2, padx=10, pady=0)
        input_last_name = Entry(input_frame, font='Nunito 18')
        input_last_name.grid(row=0,column=3, padx=10, pady=10)

        input_fathersname_text= Label(input_frame,text="Father's Name",font='Nunito 20')
        input_fathersname_text.grid(row=2,column=0, padx=10, pady=0)
        input_fathersname = Entry(input_frame, font='Nunito 18')
        input_fathersname.grid(row=2,column=1, padx=10, pady=10)

        input_mothersname_text = Label(input_frame,text="Mother's Name",font='Nunito 20')
        input_mothersname_text.grid(row=2,column=2, padx=10, pady=0)
        input_mothersname = Entry(input_frame, font='Nunito 18')
        input_mothersname.grid(row=2,column=3, padx=10, pady=10)

        input_age_text = Label(input_frame,text="Age",font='Nunito 20')
        input_age_text.grid(row=3,column=0, padx=10, pady=0)
        input_age = Entry(input_frame, font='Nunito 18')
        input_age.grid(row=3,column=1, padx=10, pady=10)

        input_citizenshipnumber_text = Label(input_frame,text="Citizenship Number",font='Nunito 20')
        input_citizenshipnumber_text.grid(row=3,column=2, padx=10, pady=0)
        input_citizenshipnumber = Entry(input_frame,font='Nunito 18')
        input_citizenshipnumber.grid(row=3,column=3, padx=10, pady=10)

        input_address_text = Label(input_frame,text='Address',font='Nunito 20')
        input_address_text.grid(row=4,column=0, padx=10, pady=0)
        input_address = Entry(input_frame,font='Nunito 18')
        input_address.grid(row=4,column=1, padx=10, pady=10)

        input_contact_text = Label(input_frame,text='Contact',font='Nunito 20')
        input_contact_text.grid(row=4,column=2, padx=10, pady=0)
        input_contact = Entry(input_frame,font='Nunito 18')
        input_contact.grid(row=4,column=3, padx=10, pady=10)

        input_education_text = Label(input_frame,text='Education',font='Nunito 20')
        input_education_text.grid(row=5,column=0, padx=10, pady=0)
        input_education = Entry(input_frame,font='Nunito 18')
        input_education.grid(row=5,column=1, padx=10, pady=10)

        input_work_text = Label(input_frame,text='Work (if any)',font='Nunito 20')
        input_work_text.grid(row=5,column=2, padx=10, pady=0)
        input_work = Entry(input_frame,font='Nunito 18')
        input_work.grid(row=5,column=3, padx=10, pady=10)


        button_login = Button(self.root,text='Register',command=getData, font='Nunito 17')
        button_login.pack(fill=X, padx=10, pady=10)

# root = Tk()
# RegisterAccount(root,26)
# root.mainloop()
