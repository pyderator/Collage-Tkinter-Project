from tkinter import *
import uuid
from con_to_sql import AdminInterfaceQuy
from tkinter.ttk import Combobox
from datetime import date
class AdminInt:
    def __init__(self,root):
        self.ins = AdminInterfaceQuy()
        self.root = root
        self.root.title('Welcome Admin')

        self.adminframe = Frame(self.root,height=500, width=500)
        self.adminframe.grid(row=0,column=0)

        self.showpendingacc = Button(self.adminframe,text=f'Pending Accounts To Review({self.ins.totacc[0][0]})',command=self.show_acc)
        self.showpendingacc.grid(row=1,column=1)

    def show_acc(self):
        self.accountsframe = Frame(self.root,height=500,width=500)
        self.accountsframe.grid(row=1,column=0)
        options = []
        for i in self.ins.accs:
            options.append(f'Id {i[0]}')
        print(options)
        self.idsel = Combobox(self.accountsframe,value=options,width='20',state='readonly')
        self.idsel.current(0)
        self.idsel.bind('<<ComboboxSelected>>',self.show_data)
        self.idsel.grid(row=1,column=1)
        self.show_data()
    def show_data(self,*args):
        # if self.dataframe:
        #     self.database.destroy()
        self.user_id = int(self.idsel.get().split()[-1])
        result = self.ins.searchid(self.user_id)

        self.acc_id = result[-1]
        print('aacc',self.acc_id)

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

        self.rejval = IntVar()
        print('res',result[10])
        self.rejval.set(result[10])
        self.input_reject_text = Label(self.dataframe,text='Reject',font='Nunito')
        self.input_reject_text.grid(row=12,column=1)
        self.radiobtn1 = Radiobutton(self.dataframe,variable=self.rejval,text='Accept',value=1,command=self.select)
        self.radiobtn1.grid(row=12,column=2)
        self.radiobtn2 = Radiobutton(self.dataframe,variable=self.rejval,text='Reject',value=0,command=self.select)
        self.radiobtn2.grid(row=12,column=3)


        self.input_remarks_text = Label(self.dataframe,text='Remarks',font='Nunito')
        self.input_remarks_text.grid(row=13,column=1)
        self.input_remark = Entry(self.dataframe)
        self.input_remark.insert(0,result[11])
        self.input_remark.grid(row=13,column=2)

        self.button_green = Button(self.dataframe,text='Create Account',command=self.createacc)
        self.button_green.grid(row=14,column=1)

        self.button_red = Button(self.dataframe, text='Send update message',command=self.updateonly)
        self.button_red.grid(row=15,column=1)

    def createacc(self):
        print(self.user_id,self.input_first_name.get(),self.input_last_name.get(),self.input_fathersname.get(),self.input_mothersname.get(),self.input_age.get(),self.input_contact.get(),uuid.uuid4(),str(date.today()),self.input_address.get())
        self.ins.insertuser(self.acc_id,self.input_first_name.get(),self.input_last_name.get(),self.input_fathersname.get(),self.input_mothersname.get(),self.input_age.get(),self.input_contact.get(),str(uuid.uuid4()),date.today(),self.input_address.get())
    def updateonly(self):
        self.ins.updateremarks(self.user_id,self.input_remark.get())
    def select(self):
        print(self.rejval.get())
