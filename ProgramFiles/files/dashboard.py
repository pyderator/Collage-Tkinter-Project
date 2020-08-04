from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


# forget password
from fpdf import FPDF, HTMLMixin
import random
import string
from con_to_sql import AccStats
from forgetpassword import ForgetPassword
from acc_reg import RegisterAccount
from con_to_sql import PendingAccount
from datetime import date
class Dashboard:
    def __init__(self,root,username,user_id):

        self.root = root
        self.user = username
        self.root.geometry('500x500')
        self.user_id = user_id
        self.accstats = AccStats(self.user_id)
        self.root.title(f"Dashboard, {self.user.upper()}")

        self.nav_frame = Frame(self.root,height=400,width=400)
        self.nav_frame.grid(row=0,column=1)

        self.nav_Home = Button(self.nav_frame,text='Home')
        self.nav_Home.grid(row=0,column=0)

        self.nav_register = Button(self.nav_frame,text='Register New Account',command=self.new_acc)
        self.nav_register.grid(row=0,column=1)

        self.nav_delete = Button(self.nav_frame,text='Pending Accounts',command=self.show_acc)
        self.nav_delete.grid(row=0,column=2)

        self.nav_status = Button(self.nav_frame,text='Account Status',command=self.accstatsfunc)
        self.nav_status.grid(row=0,column=3)

        self.nav_changepw = Button(self.nav_frame,text='Change Password',command=self.changepassword)
        self.nav_changepw.grid(row=0,column=4)

        self.root.mainloop()


    def new_acc(self):
        accountregister = Toplevel(self.root)
        RegisterAccount(accountregister,self.user_id)

    def changepassword(self):
        change_pw = Toplevel(self.root)
        ForgetPassword(change_pw)

    def accstatsfunc(self):
        accounts = self.accstats.fetchinfo()
        if len(accounts) > 0:
            self.acc_frame = Frame(self.root,height=300,width=300)
            self.acc_frame.grid(row=1,column=1)
            self.bal_frame = Frame(self.root,height=300,width=300)
            self.bal_frame.grid(row=2,column=1)
            self.acc_ids = []
            for i in accounts:
                self.acc_ids.append(i[0])
            self.acc_combobox = Combobox(self.acc_frame,values=self.acc_ids,state='readonly',width='50')
            self.acc_combobox.grid(row=0,column=0)
            self.acc_combobox.current(0)
            self.fetch_data()
            self.acc_combobox.bind('<<ComboboxSelected>>',self.fetch_data)
    def fetch_data(self,*args):
        self.bal_frame.destroy()
        # Re-rendering the frame
        self.bal_frame = Frame(self.root,height=300,width=300)
        self.bal_frame.grid(row=2,column=1)
        data = self.accstats.accountinfo(self.acc_combobox.get())
        self.regname = data[0][1] + data[0][2]
        self.datecreated = data[0][3]
        self.balances = data[1]

        if self.balances:
            pass
        else:
            self.balances = (0,0)

        self.nameLabel = Label(self.bal_frame,text=f"Account Holder Name: {self.regname}")
        self.nameLabel.grid(row=1,column=0)
        self.nameLabel = Label(self.bal_frame,text=f"Account Created Date: {self.datecreated}")
        self.nameLabel.grid(row=2,column=0)
        self.creditLabel = Label(self.bal_frame,text=f"Credit Balance: {self.balances[0]}")
        self.creditLabel.grid(row=3,column=0)
        self.debitLabel = Label(self.bal_frame, text=f"Debit Balance: {self.balances[1]}")
        self.debitLabel.grid(row=4,column=0)


        self.sendmoneyLabel = Label(self.bal_frame,text=f'Send Money')
        self.sendmoneyLabel.grid(row=5,column=0)

        self.new_acc_ids = []
        self.all_acc_ids = self.accstats.getallacc()

        for i in self.all_acc_ids:
            if self.acc_combobox.get() != i[0]:
                self.new_acc_ids.append(i[0])

        self.send_moneycb_text = Label(self.bal_frame,text='Choose Account')
        self.send_moneycb_text.grid(row=6,column=0)
        self.send_moneycb = Combobox(self.bal_frame,values=self.new_acc_ids,width='50')
        self.send_moneycb.grid(row=6,column=1)
        self.send_moneycb.current(0)

        self.amount_text = Label(self.bal_frame,text='Amount')
        self.amount_text.grid(row=7,column=0)
        self.amount_entry = Entry(self.bal_frame)
        self.amount_entry.grid(row=7,column=1)

        self.amount_text_invoice = Label(self.bal_frame,text='Invoice')
        self.amount_text_invoice.grid(row=8,column=0)
        self.amount_entry_invoice = Entry(self.bal_frame)
        self.amount_entry_invoice.grid(row=8,column=1)

        self.sendMoney = Button(self.bal_frame,text='Send Money',command=self.send_money)
        self.sendMoney.grid(row=9,column=0)

        self.esewabanner = Label(self.bal_frame,text='Load E-Sewa')
        self.esewabanner.grid(row=10,column=0)

        self.amountesewa_text = Label(self.bal_frame,text='Invoice')
        self.amountesewa_text.grid(row=11,column=0)
        self.amount_entry_esewa = Entry(self.bal_frame)
        self.amount_entry_esewa.grid(row=11,column=1)

        self.amountesewa_text_number = Label(self.bal_frame,text='Number')
        self.amountesewa_text_number.grid(row=12,column=0)
        self.number_entry_esewa = Entry(self.bal_frame)
        self.number_entry_esewa.grid(row=12,column=1)

        self.amountesewa_text_transactionInvoice = Label(self.bal_frame,text='Number')
        self.amountesewa_text_transactionInvoice.grid(row=13,column=0)
        self.number_entry_transactionInvoice = Entry(self.bal_frame)
        self.number_entry_transactionInvoice.grid(row=13,column=1)

        self.loadesewa = Button(self.bal_frame,text='Load Esewa',command=self.load_esewa)
        self.loadesewa.grid(row=13,column=0)

    def send_money(self):
        if self.accstats.transactions(self.send_moneycb.get(),self.acc_combobox.get(),self.amount_entry.get()):
            msgbox = messagebox.askquestion('Message',f'Payment Successful \n Do You Want To Save Transaction')
            if msgbox == 'yes':
                html2pdf(self.user,self.acc_combobox.get(),self.send_moneycb.get(),self.amount_entry.get(),self.amount_entry_invoice.get())

    def load_esewa(self):
        if self.accstats.esewa(self.number_entry_esewa.get(),self.acc_combobox.get(),self.amount_entry_esewa.get()):
            msgbox = messagebox.askquestion('Message',f'Payment Successful \n Do You Want To Save Transaction')
            if msgbox == 'yes':
                html2pdf(self.user,self.acc_combobox.get(),self.number_entry_esewa.get(),self.send_moneycb.get(),self.number_entry_transactionInvoice.get())


    def show_acc(self):
        self.accountsframe = Frame(self.root,height=500,width=500)
        self.accountsframe.grid(row=1,column=0)
        options = []
        for i in PendingAccount(self.user_id).accs:
            options.append(f'Id {i[0]}')
        print(options)
        self.idsel = Combobox(self.accountsframe,value=options,width='20',state='readonly')
        self.idsel.current(0)
        self.idsel.bind('<<ComboboxSelected>>',self.show_data)
        self.idsel.grid(row=1,column=1)
        self.show_data()

    def show_data(self,*args):

        self._id = int(self.idsel.get().split()[-1])
        result = PendingAccount(self._id).searchid()

        self.acc_id = result[-1]
        print('aacc',self.acc_id)

        self.uid = result[-2]
        self.dataframe = Frame(self.root, height=300,width=300)
        self.dataframe.grid(column=0,row=2)

        self.input_first_name_text = Label(self.dataframe,text='First Name',font='Nunito')
        self.input_first_name_text.grid(row=2,column=1)
        self.input_first_name = Entry(self.dataframe)
        self.input_first_name.insert(0,result[0])
        self.input_first_name.grid(row=2,column=2)

        self.input_last_name_text = Label(self.dataframe,text='Last Name',font='Nunito')
        self.input_last_name_text.grid(row=3,column=1)
        self.input_last_name = Entry(self.dataframe)
        self.input_last_name.insert(0,result[1])
        self.input_last_name.grid(row=3,column=2)

        self.input_fathersname_text= Label(self.dataframe,text="Father's Name",font='Nunito')
        self.input_fathersname_text.grid(row=4,column=1)
        self.input_fathersname = Entry(self.dataframe)
        self.input_fathersname.insert(0,result[2])
        self.input_fathersname.grid(row=4,column=2)

        self.input_mothersname_text = Label(self.dataframe,text="Mother's Name",font='Nunito')
        self.input_mothersname_text.grid(row=5,column=1)
        self.input_mothersname = Entry(self.dataframe)
        self.input_mothersname.insert(0,result[3])
        self.input_mothersname.grid(row=5,column=2)

        self.input_age_text = Label(self.dataframe,text="Age",font='Nunito')
        self.input_age_text.grid(row=6,column=1)
        self.input_age = Entry(self.dataframe)
        self.input_age.insert(0,result[4])
        self.input_age.grid(row=6,column=2)

        self.input_citizenshipnumber_text = Label(self.dataframe,text="Citizenship Number",font='Nunito')
        self.input_citizenshipnumber_text.grid(row=7,column=1)
        self.input_citizenshipnumber = Entry(self.dataframe)
        self.input_citizenshipnumber.insert(0,result[5])
        self.input_citizenshipnumber.grid(row=7,column=2)

        self.input_address_text = Label(self.dataframe,text='Address',font='Nunito')
        self.input_address_text.grid(row=8,column=1)
        self.input_address = Entry(self.dataframe)
        self.input_address.insert(0,result[6])
        self.input_address.grid(row=8,column=2)

        self.input_contact_text = Label(self.dataframe,text='Contact',font='Nunito')
        self.input_contact_text.grid(row=9,column=1)
        self.input_contact = Entry(self.dataframe)
        self.input_contact.insert(0,result[7])
        self.input_contact.grid(row=9,column=2)

        self.input_education_text = Label(self.dataframe,text='Education',font='Nunito')
        self.input_education_text.grid(row=10,column=1)
        self.input_education = Entry(self.dataframe)
        self.input_education.insert(0,result[8])
        self.input_education.grid(row=10,column=2)

        self.input_work_text = Label(self.dataframe,text='Work (if any)',font='Nunito')
        self.input_work_text.grid(row=11,column=1)
        self.input_work = Entry(self.dataframe)
        self.input_work.insert(0,result[9])
        self.input_work.grid(row=11,column=2)

        self.input_remarks_text = Label(self.dataframe,text='Remarks',font='Nunito')
        self.input_remarks_text.grid(row=13,column=1)
        self.input_remark = Label(self.dataframe,text=f'{result[10]}')
        self.input_remark.grid(row=13,column=2)

        self.button_red = Button(self.dataframe, text='Update info',command=self.updateinfo)
        self.button_red.grid(row=15,column=1)


    def updateinfo(self):
        PendingAccount(self.user_id).updateacc(self.input_first_name.get(),self.input_last_name.get(),self.input_fathersname.get(),self.input_mothersname.get(),self.input_age.get(),self.input_citizenshipnumber.get(),self.input_address.get(),self.input_contact.get(),self.input_education.get(),self.input_work.get(),self.uid)

class HTML2PDF(FPDF, HTMLMixin):
    pass

def html2pdf(sender_name,sender_acc,receiver,amount,invoice):
    transaction_id = ''.join(random.choice(string.hexdigits) for i in range(20))
    html = f'''
    <div style="width: 50%; margin: auto;">
        <h1 style="font-size: 30px; font-family: Nunito;text-align: center;">Bank Transaction</h1>
        <div style="padding: 50px 0 0 0;display: flex;width: 100%;justify-content: space-around;">
            <p style="font-family: Nunito; font-weight: 600;">Transaction Id: {transaction_id}</p>
            <p style="font-family: Nunito; font-weight: 600;">Date: {str(date.today())}</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Sender Name: {sender_name}</p>
            <p style="font-family: Nunito; font-weight: 600;">Account Id: {sender_acc}</p>
            <p style="font-family: Nunito; font-weight: 600;">Amount Sent: {amount}</p>
            <p style="font-family: Nunito; font-weight: 400;">Invoice: {invoice}</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Receiver Account Id: {receiver}</p>
        </div>
        <div style="display: flex;justify-content: flex-end;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Checked By: Online Transaction</p>
        </div>
    </div>
    '''
    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    pdf.output(f'/home/pyderator/Documents/tkinterproject/myself/Collage-Tkinter-Project/ProgramFiles/invoice/{str(sender_name)+str(transaction_id)}.pdf')
