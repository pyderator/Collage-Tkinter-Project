from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import con_to_sql as sql_conn

class RegisterAccount:
    def __init__(self,root,user_id):
        self.root = root
        root.resizable(0,0)
        root.title('Welcome To Bank')
        root.geometry('320x330')
        self.frame_login = Frame(root,height=500,width=500)
        self.frame_login.grid(row=0,column=0)
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


            register = sql_conn.AccRegAdmin(self.user_id,firstname,lastname,fathersname,mothersname,age,citizenshipnumber,location,contact,education,work)
            if register.isregistered:
                messagebox.showinfo('Congrats','Successfully Registered')

        register_text = Label(self.frame_login,text='Register Now',font='Poppins')
        register_text.grid(row=1,column=1)

        input_first_name_text = Label(self.frame_login,text='First Name',font='Nunito')
        input_first_name_text.grid(row=2,column=1)
        input_first_name = Entry(self.frame_login)
        input_first_name.grid(row=2,column=2)

        input_last_name_text = Label(self.frame_login,text='Last Name',font='Nunito')
        input_last_name_text.grid(row=3,column=1)
        input_last_name = Entry(self.frame_login)
        input_last_name.grid(row=3,column=2)

        input_fathersname_text= Label(self.frame_login,text="Father's Name",font='Nunito')
        input_fathersname_text.grid(row=4,column=1)
        input_fathersname = Entry(self.frame_login)
        input_fathersname.grid(row=4,column=2)

        input_mothersname_text = Label(self.frame_login,text="Mother's Name",font='Nunito')
        input_mothersname_text.grid(row=5,column=1)
        input_mothersname = Entry(self.frame_login)
        input_mothersname.grid(row=5,column=2)

        input_age_text = Label(self.frame_login,text="Age",font='Nunito')
        input_age_text.grid(row=6,column=1)
        input_age = Entry(self.frame_login)
        input_age.grid(row=6,column=2)

        input_citizenshipnumber_text = Label(self.frame_login,text="Citizenship Number",font='Nunito')
        input_citizenshipnumber_text.grid(row=7,column=1)
        input_citizenshipnumber = Entry(self.frame_login)
        input_citizenshipnumber.grid(row=7,column=2)

        input_address_text = Label(self.frame_login,text='Address',font='Nunito')
        input_address_text.grid(row=8,column=1)
        input_address = Entry(self.frame_login)
        input_address.grid(row=8,column=2)

        input_contact_text = Label(self.frame_login,text='Contact',font='Nunito')
        input_contact_text.grid(row=9,column=1)
        input_contact = Entry(self.frame_login)
        input_contact.grid(row=9,column=2)

        input_education_text = Label(self.frame_login,text='Education',font='Nunito')
        input_education_text.grid(row=10,column=1)
        input_education = Entry(self.frame_login)
        input_education.grid(row=10,column=2)

        input_work_text = Label(self.frame_login,text='Work (if any)',font='Nunito')
        input_work_text.grid(row=11,column=1)
        input_work = Entry(self.frame_login)
        input_work.grid(row=11,column=2)


        button_login = Button(self.frame_login,text='Login',command=getData)
        button_login.grid(row=12,column=0)
