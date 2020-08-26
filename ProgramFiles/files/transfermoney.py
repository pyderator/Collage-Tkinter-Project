from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from con_to_sql import Transaction
from topdf import html2pdf


class TransferMoney:

    def __init__(self, root, user_id):

        self.root = root
        self.root.title('Transaction')
        self.user_id = user_id
        self.transaction_class = Transaction(user_id)
        self.accIds = []

        for i in self.transaction_class.account_ids:
            self.accIds.append(i[0])
            
        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.InfoLabel = Label(self.frame1,text='Please Select AnyOne Of The Account ID',font='Nunito 20')
        self.InfoLabel.grid(row=0,column=0, padx=10, pady=10)

        self.account_datas = Combobox(self.frame1, values=self.accIds, state='readonly', width=50)
        self.account_datas.grid(row=1, column=0, padx=10, pady=10)
        self.account_datas.current(0)

        self.InfoLabel = Label(self.frame1,text='Receipent Account ID',font='Nunito 18')
        self.InfoLabel.grid(row=2,column=0, padx=10, pady=10)

        self.recept_acc_id = Entry(self.frame1, font='Nunito 16', width=30)
        self.recept_acc_id.grid(row=3,column=0, padx=10)

        self.amount = Label(self.frame1,text='Amount',font='Nunito 18')
        self.amount.grid(row=4,column=0, padx=10, pady=10)

        self.amount_entry = Entry(self.frame1, font='Nunito 16', width=30)
        self.amount_entry.grid(row=5,column=0, padx=10)

        self.invoice = Label(self.frame1,text='Invoice',font='Nunito 18')
        self.invoice.grid(row=6,column=0, padx=10)

        self.invoice_entry = Text(self.frame1, font='Nunito 16', width=30, height=10)
        self.invoice_entry.grid(row=7,column=0, padx=10)


        self.input_last_name = Button(self.frame1, font='Nunito 16', text='Send',width=30, command=self.transfer_money)
        self.input_last_name.grid(row=8,columnspan=4, padx=10, pady=10)

    def transfer_money(self):

        if self.recept_acc_id.get() == '' or self.amount_entry.get() == '' or self.invoice_entry.get("1.0",'end-1c') == '':
            messagebox.showerror('Error', 'Provide All Input')
            return False
        elif int(self.amount_entry.get()) <= 0:
            messagebox.showerror('Error', 'Provide Valid Input')
            return False

        response = Transaction(self.user_id).transfer_money(self.account_datas.get(), self.amount_entry.get(), self.recept_acc_id.get())
        if response:
            que = messagebox.askokcancel('Dear user', 'Do you wanna save this transaction ?')
            if que == 'Yes' or 'yes' or 'Ok' or 'ok':
                html2pdf(self.account_datas.get(), self.recept_acc_id.get(), self.amount_entry.get(), self.invoice_entry.get("1.0",'end-1c'))
        else:
            messagebox.showerror("Error","Something is wrong")
