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
from datetime import date
class Dashboard:
    def __init__(self,root,username,user_id):

        self.root = root
        self.user = username
        self.root.geometry('500x500')
        self.user_id = user_id
        self.accstats = AccStats(self.user_id)
        self.root.title(f'Dashboard, {self.user.upper()}')

        self.nav_frame = Frame(self.root,height=400,width=400)
        self.nav_frame.grid(row=0,column=1)

        self.nav_Home = Button(self.nav_frame,text='Home')
        self.nav_Home.grid(row=0,column=0)

        self.nav_register = Button(self.nav_frame,text='Register New Account',command=self.new_acc)
        self.nav_register.grid(row=0,column=1)

        self.nav_delete = Button(self.nav_frame,text='Delete Account')
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
