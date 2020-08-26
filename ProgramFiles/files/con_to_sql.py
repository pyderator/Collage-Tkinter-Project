import mysql.connector
from tkinter import messagebox
import sys
class Connection:

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='Bank_Users')
            self.cursor = self.cnx.cursor(buffered=True)
        except:
            messagebox.showerror('Error','Database is not connected!! Make Sure To Connect It')
            sys.exit()
            


class Login(Connection):
    '''Login's the User'''

    def __init__(self,):

        super().__init__()
        self.islogged = False

    def login(self,username,password):

        try:
             qry = """ SELECT * FROM Users WHERE username=%s AND password=%s """
             self.cursor.execute(qry,(username,password,))
             records = self.cursor.fetchone()

             if len(records) > 0:
                 messagebox.showinfo('Welcome',f'Hello {records[1]}')
                 self.islogged = True
                 self.user_id = records[0]
                 if records[-1] == 'admin':
                     self.is_admin=True
                 else:
                     self.is_admin= False
             else:
                 messagebox.showerror('Opps','Something is wrong')
        except:
            messagebox.showerror('Error','Username or password is wrong')
            return False


class Register(Connection):
    """Registers the user"""

    def __init__(self):
        super().__init__()

    def register(self,*args):

        try:
            qry1 ="INSERT INTO Users (first_name,last_name,username,password,age,address,contact) values (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(qry1,(args[0],args[1],args[2],args[3],args[4],args[5],args[6]))
            self.cnx.commit()

            qry2 = "SELECT id from Users WHERE username = %s"
            self.cursor.execute(qry2,(args[2],))
            user_id = self.cursor.fetchone()[0]

            qry3 = 'INSERT INTO Questions (user_id,Question_id,answer) values (%s,%s,%s)'
            self.cursor.execute(qry3,(user_id,args[7],args[8]))
            self.cnx.commit()
            return True

        except:

            return False


class RecoverPassword(Connection):

    '''Reset the user's password'''
    def __init__(self,*args):
        super().__init__()

    def login(self,*args):
        '''Checks if user exists or not'''
        try:
             qry = """SELECT * FROM Users WHERE username=%s"""
             self.cursor.execute(qry,(args[0],))
             self.records = self.cursor.fetchone()

             if self.records:
                 return self.records[0]
             else:
                 return False
        except:
            messagebox.showerror('Error','Something Went Wrong')

    def recoverpassword(self,data):
        '''Fetchs the question_id and answer of that particular question'''
        try:
            qry = "SELECT question_id,answer from Questions WHERE user_id = %s"
            self.cursor.execute(qry,(data,))
            records = self.cursor.fetchone()
            return records
        except:
            messagebox.showerror('Error','Something Went Wrong!!')

    def changepassword(self, newpassword):
        '''Changes the user password'''
        try:

            qry = "UPDATE Users SET password = %s WHERE id = %s"
            a = self.cursor.execute(qry,( newpassword, self.records[0]))
            self.cnx.commit()
        except:
            messagebox.showerror('Error','Something Went Wrong!!')


class AccRegAdmin(Connection):
    """  Registers an account and sends to user for verification  """

    def __init__(self,*args):
        self.isregistered=False
        super(AccRegAdmin, self).__init__()
        self.regacc(*args)

    def regacc(self,*args):

        qry = "INSERT INTO Acc_to_check (user_id,First_Name,Last_Name,Fathers_Name,Mothers_Name,Age,Citizenship_Number,Location,Contact,Education,Work) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(qry, (args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],))
        self.cnx.commit()
        self.isregistered=True


class Account_manager(Connection):
    """Looks after the user accounts"""

    def __init__(self, user_id=None):
        super(Account_manager, self).__init__()
        self.user_id = user_id

    def fetch_account_info(self):
        qry = f"""

            SELECT a.id, a.Account_id, a.created_time,b.Credit_Amount, b.Debit_Amount
            FROM Accounts AS a
            JOIN Balance AS b ON a.id = b.acc_id WHERE a.user_id = {self.user_id} ORDER BY first_name desc

        """
        self.cursor.execute(qry)
        res = self.cursor.fetchall()
        return res

    def pending_account_info(self):
        qry = f"""

            SELECT id, First_Name, Last_Name, Fathers_Name, Mothers_Name, Age, Citizenship_Number, Location, Contact, Education, Work, Remarks FROM Acc_to_check WHERE Acc_to_check.user_id = {self.user_id} AND Acc_to_check.is_rejectable=0

        """
        self.cursor.execute(qry)
        return self.cursor.fetchall()

    def update_pending_acc(self,data,acc_id):
        try:
            text = 'UPDATE Acc_to_check SET '
            for i in range(len(data)):
            	for j,k in data[i].items():
            		text += f"{j} = '{k}',"

            qry = text[:-1] + f' WHERE id = {acc_id}'
            self.cursor.execute(qry)
            self.cnx.commit()
        except Exception as e:
            return False
        else:
            return True


class AdminInterface(Connection):

    def __init__(self):
        super().__init__()

    def pending_account_info(self):
        qry = f"""

            SELECT id, First_Name, Last_Name, Fathers_Name, Mothers_Name, Age, Citizenship_Number, Location, Contact, Education, Work, Remarks FROM Acc_to_check WHERE Acc_to_check.is_rejectable=0

        """
        self.cursor.execute(qry)
        return self.cursor.fetchall()

    def update_pending_acc(self,data,acc_id):
        try:
            text = 'UPDATE Acc_to_check SET '
            for i in range(len(data)):
            	for j,k in data[i].items():
            		text += f"{j} = '{k}',"

            qry = text[:-1] + f' WHERE id = {acc_id}'
            self.cursor.execute(qry)
            self.cnx.commit()
        except Exception as e:
            return False
        else:
            return True

    def create_user_account(self, acc_id, first_name, last_name, fathersname, mothersname, age, contact, account_id, created_time, location):
        try:
            qry = f"""
            UPDATE Acc_to_check SET is_rejectable = 1 WHERE id = {acc_id}
            """
            self.cursor.execute(qry)
            self.cnx.commit()
            self.cursor.execute(f'SELECT user_id FROM Acc_to_check WHERE id = {acc_id}')
            user_id = self.cursor.fetchone()[0]

            qry1 = f'''
            INSERT INTO Accounts (user_id, first_name, last_name, fathersname, mothersname, age, contact, Account_id, created_time, location) values {user_id, first_name, last_name, fathersname, mothersname, age, contact, account_id, created_time, location}
            '''
            self.cursor.execute(qry1)
            self.cnx.commit()

            qry2 = f'''SELECT id from Accounts WHERE user_id = {user_id}'''
            self.cursor.execute(qry2)
            acc_id1 = self.cursor.fetchone()[0]

            qry3 = f'''INSERT INTO Balance (acc_id, Credit_Amount, Debit_Amount) VALUES ({acc_id1},500,500)'''
            self.cursor.execute(qry3)
            self.cnx.commit()
        except Exception as e:
            return False
        else:
            return True


class Transaction(Connection):
    """docstring for Transaction."""

    def __init__(self, user_id):
        super(Transaction, self).__init__()
        self.user_id = user_id
        qry = f"SELECT Account_id FROM Accounts WHERE user_id = {self.user_id}"
        self.cursor.execute(qry)
        self.account_ids = self.cursor.fetchall()

    def transfer_money(self, account_number, amount, receiver_account_number):
        try:
            qry =f"""SELECT b.Debit_Amount FROM Balance as b JOIN Accounts as a ON a.id = b.acc_id WHERE a.Account_id='{account_number}'"""

            self.cursor.execute(qry)
            balance = self.cursor.fetchone()[0]
            if int(balance) < int(amount):
                messagebox.showerror('Error', 'Not Enough Balance :(')
                return False

            qry1 =f"""UPDATE Balance INNER JOIN Accounts ON Accounts.id = Balance.acc_id SET Debit_Amount = '{int(balance)-int(amount)}' WHERE Accounts.Account_id ='{account_number}'"""
            self.cursor.execute(qry1)
            self.cnx.commit()

            qry2 =f"""UPDATE Balance INNER JOIN Accounts ON Accounts.id = Balance.acc_id SET Debit_Amount = Credit_Amount + '{amount}' WHERE Accounts.Account_id ='{receiver_account_number}'"""
            self.cursor.execute(qry2)
            self.cnx.commit()
        except Exception as e:
            return False
        else:
            return True

    def load_esewa(self,account_number, amount):
        try:
            qry =f"""SELECT b.Debit_Amount FROM Balance as b JOIN Accounts as a ON a.id = b.acc_id WHERE a.Account_id='{account_number}'"""

            self.cursor.execute(qry)
            balance = self.cursor.fetchone()[0]
            if int(balance) < int(amount):
                messagebox.showerror('Error', 'Not Enough Balance :(')
                return False

            qry1 =f"""UPDATE Balance INNER JOIN Accounts ON Accounts.id = Balance.acc_id SET Debit_Amount = '{int(balance)-int(amount)}' WHERE Accounts.Account_id ='{account_number}'"""
            self.cursor.execute(qry1)
            self.cnx.commit()

        except Exception as e:
            return False

        else:
            return True
