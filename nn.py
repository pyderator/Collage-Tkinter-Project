
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title('User Form')
        self.window.geometry('1199x900+100+50')
        self.window.resizable(0, 0)

        self.frame1 = Frame(self.window, bg='white')
        self.frame1.place(x=400, y=90, height=400, width=450)
        self.title = Label(self.frame1, text='Login Here', font=('Impact', 20, 'bold'), fg="#d77337", bg='white').place(
            x=50, y=15)
        self.desc = Label(self.frame1, text='Airline Ticket Login Area', font=('Goudy old style', 12), fg="#d25d17",
                          bg='white').place(x=50, y=50)

        self.lb_code = Label(self.frame1, text='Email', font=('Goudy old style', 15, 'bold'), fg='grey',
                             bg='white').place(x=50, y=90)
        self.ent_code = Entry(self.frame1, font=('times new roman', 10), bg='lightgray')
        self.ent_code.place(x=50, y=140, width=260, height=30)
        self.pw_code = Label(self.frame1, text='Password', font=('Goudy old style', 15, 'bold'), fg='grey',
                             bg='white').place(x=50, y=180)
        self.ent_pw = Entry(self.frame1, font=('times new roman', 10), bg='lightgray')
        self.ent_pw.place(x=50, y=220, width=260, height=30)
        self.btn1 = Button(self.window, text='signup', relief=RAISED, bg='#d77337', font=('arial', 14, 'bold'),
                           fg='white', command=self.sign_up)
        self.btn1.place(x=10, y=6)
        self.btn2 = Button(self.window, text='search Flight', relief=RAISED, bg='#d77337', font=('arial', 14, 'bold'),
                           fg='white')
        self.btn2.place(x=90, y=6)
        self.btn3 = Button(self.frame1, text='Login', relief=RAISED, bg='#d77337', font=('arial', 14, 'bold'),
                           fg='white', command=self.login_function)
        self.btn3.place(x=160, y=340, width=180)
        self.btn4 = Button(self.window, text='Exit', relief=RAISED, bg='#d77337', font=('arial', 14, 'bold'),
                           fg='white', command=exit)
        self.btn4.place(x=1100, y=6, width=80)
        self.btn5 = Button(self.frame1, text='Forget password?', bg='white', font=('times new roman', 12, 'bold'),
                           fg='#d25d17', bd=0, command=self.forget_password)
        self.btn5.place(x=50, y=280)
        # self.window.mainloop()

    def login_function(self):
        if self.ent_code.get() == "" or self.ent_pw.get() == "":
            messagebox.showerror('error', 'all fields are required', parent=self.window)

        # elif self.ent_code.get() != "Hricha" or self.ent_pw.get() != "123456":
        #     messagebox.showerror('error', 'Invalid username or password', parent=self.window)
        else:
            try:
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username or Password', parent=self.window)

                else:
                    messagebox.showinfo('Success', 'Welcome', parent=self.window)
            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)
            # print(self.ent_code.get(), self.ent_pw.get())
            # messagebox.showinfo('welcome user', parent=self.window)

    def forget_password(self):
        self.window2 = Toplevel()
        self.window2.title('Forget Password')
        self.window2.geometry('350x300+490+150')
        self.window2.config(bg='white')
        self.window2.focus_force()
        self.window2.grab_set()
        t = Label(self.window2, text='Verify Email', font=('times new roman', 20, 'bold'), bg='white',
                  fg='red').place(x=0, y=10, relwidth=1)

        self.lb_email = Label(self.window2, text='Email', font=('Goudy old style', 15, 'bold'), fg='grey',
                              bg='white').place(x=50, y=90)
        self.ent_code = Entry(self.window2, font=('times new roman', 10), bg='lightgray')
        self.ent_code.place(x=50, y=140, width=260, height=30)

        self.btn1 = Button(self.window2, text='Login', relief=RAISED, bg='#d77337', font=('arial', 14, 'bold'),
                           fg='white', command=self.verification)
        self.btn1.place(x=100, y=210, width=180)

    def verification(self):

        if self.ent_code.get() == "":
            messagebox.showerror('Error', 'Please enter the email address to reset your password', parent=self.window)

        else:
            try:
                # con = mysql.connector.connect(host='localhost', user='root', password='', database='register')
                # cur = con.cursor()
                # cur.execute('select * from users where email=%s', (self.ent_code.get(),))
                # # row = cur.fetchone()
                # if row == None:
                #     messagebox.showerror('Error', 'Please enter valid email', parent=self.window)

                self.window2 = Toplevel()
                self.window2.title('Forget Password')
                self.window2.geometry('350x400+490+150')
                self.window2.config(bg='white')
                self.window2.focus_force()
                self.window2.grab_set()
                t = Label(self.window2, text='Forget Password', font=('times new roman', 20, 'bold'), bg='white',
                          fg='red').place(x=0, y=10, relwidth=1)
                qst = Label(self.window2, text='Security Question', font=('times new roman', 15, 'bold'),
                                 bg='white',
                                 fg='gray').place(x=50, y=100)

                txt_qst = ttk.Combobox(self.window2, font=('times new roman', 13), state='readonly',
                                            justify=CENTER)
                txt_qst['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place?', 'Your NickName?')
                txt_qst.place(x=50, y=130, width=250)
                txt_qst.current(0)
                answer = Label(self.window2, text='Answer', font=('times new roman', 15, 'bold'), bg='white',
                                    fg='gray').place(
                    x=50, y=180)
                txt_answer = Entry(self.window2, font=('times new roman', 15), bg='lightgrey')
                txt_answer.place(x=50, y=210, width=250)
                new_pw = Label(self.window2, text='New Password', font=('times new roman', 15, 'bold'),
                                    bg='white',
                                    fg='gray').place(
                    x=50, y=260)
                txt_new_pw = Entry(self.window2, font=('times new roman', 15), bg='lightgrey')
                txt_new_pw.place(x=50, y=290, width=250)
                self.lambda_function = lambda : self.answer_match(txt_qst, txt_answer, txt_new_pw)
                btn_change_password = Button(self.window2, text='Reset Password', bg='green', fg='white',
                                             font=('times new roman', 15, 'bold'), command=self.lambda_function).place(
                    x=90, y=340)



            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)
            # print(self.ent_code.get(), se

    def answer_match(self,a,b,c):
        print(a.get(),b.get(),c.get())
        # if self.txt_qst.get() == "Select" or self.txt_answer.get() == "" or self.new_pw.get() == "":
        #
        #     messagebox.showerror('Error', 'All fields are required', parent=self.window2)
        #
        # else:
        #     try:
        #         con = mysql.connector.connect(host='localhost', user='root', password='', database='register')
        #         cur = con.cursor()
        #         cur.execute('select * from users where email=%s and question=&s and answer=%s',
        #                     (self.ent_code.get(), self.txt_qst.get(), self.txt_answer.get()))
        #         row = cur.fetchall()
        #         if row == None:
        #             messagebox.showerror('Error', 'Please select correct security question', parent=self.window)
        #         else:
        #             cur.execute('update users set password=%s where email=%s ',
        #                         (self.ent_code.get(), self.txt_new_pw.get()))
        #             con.commit()
        #             messagebox.showinfo('Success')
        #     except Exeption as e:
        #
        #         messagebox.showerror('error', f'error:{str(e)}', parent=self.window)

    def sign_up(self):
        self.window.withdraw()
        dd = Toplevel(self.window)
        signin.User_Form(dd)


window = Tk()
obj = Login(window)
window.mainloop()
