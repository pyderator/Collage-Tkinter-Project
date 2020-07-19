import mysql.connector
from tkinter import messagebox
class Connection:

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='Bank_Users')
            self.cursor = self.cnx.cursor()
        except:
            messagebox.showerror('Error','Database is not connected!! Make Sure To Connect It')

class Login(Connection):
    def __init__(self,*args):
        super().__init__()
        self.login(args[0],args[1])

    def login(self,*args):
        try:
             qry = """SELECT * FROM Users WHERE username=%s AND password=%s"""
             self.cursor.execute(qry,(args[0],args[1],))
             records = self.cursor.fetchall()
             print(records)
             if records:
                 print('inside',records)
                 messagebox.showinfo('Welcome',f'Hello {records[0][1]}')
             else:
                 messagebox.showerror('Opps','Something is wrong')
        except:
            messagebox.showerror('Error','Something is wrong! /n Please Try Again Later')

class Register(Connection):

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
    def __init__(self,*args):
        super().__init__()

    def login(self,*args):
        try:
             qry = """SELECT * FROM Users WHERE username=%s"""
             self.cursor.execute(qry,(args[0],))
             self.records = self.cursor.fetchone()

             if self.records:
                 return self.records[0]
             else:
                 return False
        except:
            messagebox.showerror('Error','Something Went Wring')

    def recoverpassword(self,data):
        try:
            qry = "SELECT question_id,answer from Questions WHERE user_id = %s"
            self.cursor.execute(qry,(data,))
            records = self.cursor.fetchone()
            return records
        except:
            messagebox.showerror('Error','Something Went Wrong!!')

    def changepassword(self, newpassword):
        try:

            qry = "UPDATE Users SET password = %s WHERE id = %s"
            a = self.cursor.execute(qry,( newpassword, self.records[0]))
            self.cnx.commit()
        except:
            messagebox.showerror('Error','Something Went Wrong!!')
