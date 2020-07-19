from tkinter import *
import con_to_sql as sql_conn
class RegisterPage:
    def __init__(self,root):
        self.root = root
        root.title('Welcome To Bank')
        root.geometry('500x500')

        self.frame_login = Frame(root,height=300,width=300)
        self.frame_login.grid(row=0,column=0)
        self.register()

    def register(self):

        def getData():
            first_name = input_first_name.get()
            last_name = input_last_name.get()
            username = input_username.get()
            password = input_password.get()
            address = input_address.get()
            contact = input_contact.get()
            age = input_age.get()
            sql_conn.Register(first_name,last_name,username,password,age,address,contact)


        register_text = Label(self.frame_login,text='Register Now',font='Oasis')
        register_text.grid(row=1,column=1)

        input_first_name_text = Label(self.frame_login,text='First Name:',font='Nunito')
        input_first_name_text.grid(row=2,column=1)
        input_first_name = Entry(self.frame_login)
        input_first_name.grid(row=2,column=2)

        input_last_name_text = Label(self.frame_login,text='Last Name',font='Nunito')
        input_last_name_text.grid(row=3,column=1)
        input_last_name = Entry(self.frame_login)
        input_last_name.grid(row=3,column=2)

        input_username_text= Label(self.frame_login,text='Username',font='Nunito')
        input_username_text.grid(row=4,column=1)
        input_username = Entry(self.frame_login)
        input_username.grid(row=4,column=2)

        input_password_text = Label(self.frame_login,text='Password',font='Nunito')
        input_password_text.grid(row=5,column=1)
        input_password = Entry(self.frame_login)
        input_password.grid(row=5,column=2)

        input_address_text = Label(self.frame_login,text='Address',font='Nunito')
        input_address_text.grid(row=6,column=1)
        input_address = Entry(self.frame_login)
        input_address.grid(row=6,column=2)

        input_contact_text = Label(self.frame_login,text='Contact',font='Nunito')
        input_contact_text.grid(row=7,column=1)
        input_contact = Entry(self.frame_login)
        input_contact.grid(row=7,column=2)

        input_age_text = Label(self.frame_login,text='Age',font='Nunito')
        input_age_text.grid(row=8,column=1)
        input_age = Entry(self.frame_login)
        input_age.grid(row=8,column=2)

        button_login = Button(text='Login',command=getData)
        button_login.grid(row=4,column=1)



root = Tk()
RegisterPage(root)
root.mainloop()
