import mysql.connector
from tkinter import messagebox
import sys
class Connection:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='Bank_Users')
            self.cursor = self.cnx.cursor()
        except:
            messagebox.showerror('Error','Database is not connected!! Make Sure To Connect It')
            sys.exit()

class Login(Connection):
    '''Login's the User'''
    def __init__(self,*args):
        super().__init__()
        self.islogged = False
        self.login(args[0],args[1])

    def login(self,*args):
        try:
             qry = """SELECT * FROM Users WHERE username=%s AND password=%s"""
             self.cursor.execute(qry,(args[0],args[1],))
             records = self.cursor.fetchone()
             print(records)
             if len(records) > 0:
                 messagebox.showinfo('Welcome',f'Hello {records[1]}')
                 self.islogged = True
                 self.user_id = records[0]
                 self.isadmin = records[-1]
             else:
                 messagebox.showerror('Opps','Something is wrong')
        except:
            messagebox.showerror('Error','Username or password is wrong')
            return False

class Register(Connection):
    """Registers the user"""
    def __init__(self,firstname,lastname,username,password,age,address,contact,question_id,question_answer):

        super().__init__()
        self.register(firstname,lastname,username,password,age,address,contact,question_id,question_answer)

    def register(self,*args):
        try:

            qry1 ="INSERT INTO Users (first_name,last_name,username,password,age,address,contact) values (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(qry1,(args[0],args[1],args[2],args[3],args[4],args[5],args[6]))
            self.cnx.commit()

            qry2 = "SELECT id from Users WHERE username = %s"
            self.cursor.execute(qry2,(args[2],))
            user_id = self.cursor.fetchall()
            user_id_id =user_id[0][0]

            qry3 = 'INSERT INTO Questions (user_id,Question_id,answer) values (%s,%s,%s)'
            self.cursor.execute(qry3,(user_id_id,args[7],args[8]))
            self.cnx.commit()
        except:
            messagebox.showerror('Error','Something Went Wrong!!')


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

    def __init__(self,*args):
        self.isregistered=False
        super(AccRegAdmin, self).__init__()
        self.regacc(*args)

    def regacc(self,*args):
        print(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9])
        qry = "INSERT INTO Acc_to_check (user_id,First_Name,Last_Name,Fathers_Name,Mothers_Name,Age,Citizenship_Number,Location,Contact,Education,Work) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(qry, (args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],))
        self.cnx.commit()
        self.isregistered=True


class AdminInterfaceQuy(Connection):
    def __init__(self,*args):
        super().__init__()
        qry = "SELECT COUNT(*) FROM Acc_to_check where is_rejectable=0"
        self.cursor.execute(qry)
        self.totacc = self.cursor.fetchall()

        qry1 = "SELECT * FROM Acc_to_check where is_rejectable=0"
        self.cursor.execute(qry1)
        self.accs = self.cursor.fetchall()
    def searchid(self,user_id):
        qry = "SELECT First_Name,Last_Name,Fathers_Name,Mothers_Name,Age,Citizenship_Number,Location,Contact,Education,Work,is_rejectable,Remarks,user_id FROM Acc_to_check WHERE id=%s"
        self.cursor.execute(qry,(user_id,))
        self.parAcc = self.cursor.fetchone()
        return self.parAcc

    def insertuser(self,*args):
        qry = "INSERT INTO Accounts (user_id,first_name,last_name,fathersname,mothersname,age,contact,Account_id,created_time,location) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        qry2 = "INSERT INTO Balance(acc_id,Credit_Amount,Debit_Amount) VALUES (%s,%s,%s)"
        qry1 = "SELECT id FROM Accounts WHERE Account_id = %s"
        self.cursor.execute(qry,(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],))
        self.cnx.commit()
        print('111',args[0])
        self.cursor.execute(qry1,(args[7],))
        acc_id = self.cursor.fetchone()[0]

        self.cursor.execute(qry2,(acc_id,0,0))
        self.cnx.commit()
    def updateremarks(self,*args):
        print(args)
        qry = "UPDATE Acc_to_check SET Remarks = %s WHERE id = %s"
        self.cursor.execute(qry,(args[1],args[0],))
        self.cnx.commit()

    def updaterejection(self,*args):
        qry = "UPDATE Acc_to_check SET is_rejectable = %s WHERE id = %s"
        self.cursor.execute(qry,(args[1],args[0],))
        self.cnx.commit()


class AccStats(Connection):
    def __init__(self,user_id):
        self.user_id = user_id
        print(self.user_id)
        super(AccStats,self).__init__()

    def fetchinfo(self):
        qry = "SELECT Account_id FROM Accounts WHERE user_id = %s"
        self.cursor.execute(qry,(self.user_id,))
        return self.cursor.fetchall()

    def accountinfo(self,*args):
        qry1 = "SELECT id,first_name,last_name,created_time FROM Accounts WHERE Account_id = %s"
        self.cursor.execute(qry1,(args[0],))
        acc_info =  self.cursor.fetchone()

        qry2 = "SELECT Credit_Amount,Debit_Amount FROM Balance WHERE acc_id = %s"
        self.cursor.execute(qry2,(acc_info[0],))
        balance_info = self.cursor.fetchone()

        return (acc_info,balance_info)

    def getallacc(self):
        qry1 = "SELECT Account_id FROM Accounts"
        self.cursor.execute(qry1)
        return self.cursor.fetchall()

    def transactions(self,*args):
        print('the rags',args)
        qry1= "SELECT id from Accounts where Account_id = %s"
        qry2= "SELECT id from Accounts where Account_id = %s"
        qry3= "UPDATE Balance SET Debit_Amount = Debit_Amount+ %s WHERE acc_id = %s";
        qry4= "UPDATE Balance SET Debit_Amount = Debit_Amount - %s WHERE acc_id = %s";
        qry5 = "SELECT Debit_Amount FROM Balance WHERE acc_id=%s"
        #to,from,amount
        self.cursor.execute(qry1,(args[0],))
        to_ = self.cursor.fetchone()[0]
        self.cursor.execute(qry2,(args[1],))
        from_ = self.cursor.fetchone()[0]

        from_balance = self.cursor.execute(qry5,(from_,))
        balance = self.cursor.fetchone()[0]
        if int(balance) < int(args[2]):
            messagebox.showerror('Error',f"Not Enough Balance. Total Balance Aviliable is {balance}")
            return False

        self.cursor.execute(qry3,(args[2],to_))
        self.cnx.commit()

        self.cursor.execute(qry4,(args[2],from_))
        self.cnx.commit()
        return True

    def esewa(self,*args):
        qry1= "SELECT id from Accounts where Account_id = %s"
        qry2= "UPDATE Balance SET Debit_Amount = Debit_Amount - %s WHERE acc_id = %s";
        qry3 = "SELECT Debit_Amount FROM Balance WHERE acc_id=%s"

        #to,from,amount
        self.cursor.execute(qry1,(args[1],))
        from_ = self.cursor.fetchone()[0]


        from_balance = self.cursor.execute(qry3,(from_,))
        balance = self.cursor.fetchone()[0]
        if int(balance) < int(args[2]):
            messagebox.showerror('Error',f"Not Enough Balance. Total Balance Aviliable is {balance}")
            return False

        self.cursor.execute(qry2,(args[0],from_))
        self.cnx.commit()
        return True


class PendingAccount(Connection):
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        qry1 = "SELECT * FROM Acc_to_check where is_rejectable=0 AND user_id = %s"
        self.cursor.execute(qry1,(user_id,))
        self.accs = self.cursor.fetchall()

    def searchid(self):
        qry = "SELECT First_Name,Last_Name,Fathers_Name,Mothers_Name,Age,Citizenship_Number,Location,Contact,Education,Work,Remarks,id,user_id FROM Acc_to_check WHERE user_id=%s"
        self.cursor.execute(qry,(self.user_id,))
        self.parAcc = self.cursor.fetchone()
        print(self.parAcc)
        return self.parAcc

    def updateacc(self,*args):
        try:
            qry = "UPDATE Acc_to_check SET First_Name = %s,Last_Name = %s,Fathers_Name = %s,Mothers_Name = %s,Age = %s,Citizenship_Number=%s,Location=%s,Contact=%s,Education=%s,Work=%s WHERE id = %s"
            values = (args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],)
            self.cursor.execute(qry,values)
            self.cnx.commit()
        except:
            messagebox.showerror("Error","Something Went Wrong")
        else:
            messagebox.showinfo(":)","Successfully Updated.!!")
