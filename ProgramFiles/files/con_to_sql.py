import mysql.connector

class Connection:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='Bank_Users')
        self.cursor = self.cnx.cursor()

class Login(Connection):
    def __init__(self,*args):
        super().__init__()
        self.login(args[0],args[1])

    def login(self,*args):
         print('The args',args)
         qry = """SELECT * FROM Users WHERE username=%s AND password=%s"""
         self.cursor.execute(qry,(args[0],args[1],))
         records = self.cursor.fetchall()
         print(records)

class Register(Connection):

    def __init__(self,firstname,lastname,username,password,age,address,contact):
        super().__init__()
        self.register(firstname,lastname,username,password,age,address,contact)
    def register(self,*args):
        qry ="""INSERT INTO Users values(%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(qry,(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],))
        print('success')
