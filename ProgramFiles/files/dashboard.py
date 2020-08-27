from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from transfermoney import TransferMoney
from forgetpassword import ForgetPassword
from acc_reg import RegisterAccount
from con_to_sql import Account_manager
from datetime import date
from account_status import Show_Account
from PendingAccount import PendingAccounts
from esewa import LoadEsewa


class Dashboard:

    def __init__(self,root,username,user_id):

        self.root = root
        self.user = username
        self.root.geometry('500x150')
        self.user_id = user_id
        self.root.title(f"Dashboard, {self.user}")
        dashboard_menu = Menu(self.root)
        self.root.config(menu=dashboard_menu)

        account_menu = Menu(dashboard_menu, tearoff=0)
        dashboard_menu.add_cascade(label='Account  |', menu=account_menu)
        account_menu.add_command(label='New Account', command=self.new_acc)
        account_menu.add_command(label='Pending Accounts', command=self.pending_accounts)
        account_menu.add_command(label='Account Status', command=self.account_status)
        account_menu.add_command(label='Change Password', command=self.changepassword)
        account_menu.add_command(label='Logout', command=lambda: root.destroy())



        transactions_menu = Menu(dashboard_menu, tearoff=0)
        dashboard_menu.add_cascade(label='Transactions  |', menu=transactions_menu)
        transactions_menu.add_command(label='Transfer Money',command=self.transfermoney)
        transactions_menu.add_command(label='Load Esewa', command=self.loadesewa)

        # Buttons

        self.transfer_btn = Button(self.root, font='Nunito 16', text='Send Money',width=30, command=self.transfermoney)
        self.transfer_btn.pack(fill=X, padx=10, pady=10)

        self.esewa_btn = Button(self.root, font='Nunito 16', text='Load Esewa',width=30, command=self.loadesewa)
        self.esewa_btn.pack(fill=X, padx=10, pady=10)

    def new_acc(self):
        accountregister = Toplevel(self.root)
        RegisterAccount(accountregister,self.user_id)

    def changepassword(self):
        change_pw = Toplevel(self.root)
        ForgetPassword(change_pw, self.user)

    def account_status(self):
        self.status = Account_manager(self.user_id).fetch_account_info()
        status_win = Tk()
        Show_Account(status_win).show_view(self.status)

    def pending_accounts(self):
        self.pen_accs = Account_manager(self.user_id).pending_account_info()
        if self.pen_accs:
            pending_accounts_info_win = Toplevel(self.root)
            PendingAccounts(pending_accounts_info_win).show_data(self.pen_accs)
        else:
            messagebox.showinfo('Dear Customer','There are currently no pending accounts')

    def transfermoney(self):
        transfer_money = Toplevel()
        TransferMoney(transfer_money, self.user_id)

    def loadesewa(self):
        load_esewa = Toplevel()
        LoadEsewa(load_esewa, self.user_id)
