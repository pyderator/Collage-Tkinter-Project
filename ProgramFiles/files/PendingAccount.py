from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from con_to_sql import Account_manager

class PendingAccounts:
    def __init__(self, root):
        self.root = root
        self.root.title("Pending Accounts")


        self.tree_view_frame = Frame(self.root, height=400 , width=200)
        self.tree_view_frame.pack()
        self.dataframe = Frame(self.root, height=400 , width=200)
        self.dataframe.pack()


    def show_data(self, datas):
        scroll_x1 = Scrollbar(self.tree_view_frame, orient=HORIZONTAL)
        scroll_y1 = Scrollbar(self.tree_view_frame, orient=VERTICAL)

        #Inactive Students Tree View

        self.account_view = ttk.Treeview(self.tree_view_frame, selectmode='browse', columns=(
            'First Name', 'Last Name', 'Fathers Name', 'Mothers Name','Age','Citizenship Number'
            ,'Location','Contact', 'Education', 'Work', "Remarks"),
                                          xscrollcommand=scroll_x1.set, yscrollcommand=scroll_y1.set)
        scroll_x1.pack(side=BOTTOM, fill=X)
        scroll_y1.pack(side=RIGHT, fill=Y)
        scroll_x1.config(command=self.account_view.xview)
        scroll_y1.config(command=self.account_view.yview)
        self.account_view.heading('First Name', text="First Name")
        self.account_view.heading('Last Name', text="Last Name")
        self.account_view.heading('Fathers Name', text="Fathers Name")
        self.account_view.heading('Mothers Name', text="Mothers Name")
        self.account_view.heading('Age', text="Age")
        self.account_view.heading('Citizenship Number', text="Citizenship Number")
        self.account_view.heading('Location', text="Location")
        self.account_view.heading('Contact', text="Contact")
        self.account_view.heading('Education', text="Education")
        self.account_view.heading('Work', text="Work")
        self.account_view.heading('Remarks', text="Remarks")

        self.account_view['show'] = 'headings'
        self.account_view.column('First Name', width=200, anchor='center')
        self.account_view.column('Last Name', width=200, anchor='center')
        self.account_view.column('Fathers Name', width=200, anchor='center')
        self.account_view.column('Mothers Name', width=200, anchor='center')
        self.account_view.column('Age', width=200, anchor='center')
        self.account_view.column('Citizenship Number', width=200, anchor='center')
        self.account_view.column('Location', width=200, anchor='center')
        self.account_view.column('Contact', width=200, anchor='center')
        self.account_view.column('Education', width=200, anchor='center')
        self.account_view.column('Work', width=200, anchor='center')
        self.account_view.column('Remarks', width=200, anchor='center')
        self.account_view.bind('<Double-1>', self.entry_data)


        self.account_view.pack(fill=BOTH, expand=1)
        for i in datas:
            self.account_view.insert('','end', text=i[0], values=(i[1],i[2], i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))

        self.input_first_name_text = Label(self.dataframe,text='First Name',font='Nunito 20')
        self.input_first_name_text.grid(row=0,column=0, padx=10, pady=10)
        self.input_first_name = Entry(self.dataframe, font='Nunito 16')
        self.input_first_name.grid(row=0,column=1, padx=10, pady=10)

        self.input_last_name_text = Label(self.dataframe,text='Last Name',font='Nunito 20')
        self.input_last_name_text.grid(row=0,column=2, padx=10, pady=10)
        self.input_last_name = Entry(self.dataframe, font='Nunito 16')
        self.input_last_name.grid(row=0,column=3, padx=10, pady=10)

        self.input_fathersname_text= Label(self.dataframe,text="Father's Name",font='Nunito 20')
        self.input_fathersname_text.grid(row=1,column=0, padx=10, pady=10)
        self.input_fathersname = Entry(self.dataframe, font='Nunito 16')
        self.input_fathersname.grid(row=1,column=1, padx=10, pady=10)

        self.input_mothersname_text = Label(self.dataframe,text="Mother's Name",font='Nunito 20')
        self.input_mothersname_text.grid(row=1,column=2, padx=10, pady=10)
        self.input_mothersname = Entry(self.dataframe, font='Nunito 16')
        self.input_mothersname.grid(row=1,column=3, padx=10, pady=10)

        self.input_age_text = Label(self.dataframe,text="Age",font='Nunito 20')
        self.input_age_text.grid(row=2,column=0, padx=10, pady=10)
        self.input_age = Entry(self.dataframe, font='Nunito 16')
        self.input_age.grid(row=2,column=1, padx=10, pady=10)

        self.input_citizenshipnumber_text = Label(self.dataframe,text="Citizenship Number",font='Nunito 20')
        self.input_citizenshipnumber_text.grid(row=2,column=2, padx=10, pady=10)
        self.input_citizenshipnumber = Entry(self.dataframe, font='Nunito 16')
        self.input_citizenshipnumber.grid(row=2,column=3, padx=10, pady=10)

        self.input_address_text = Label(self.dataframe,text='Address',font='Nunito 20')
        self.input_address_text.grid(row=3,column=0, padx=10, pady=10)
        self.input_address = Entry(self.dataframe, font='Nuntio 16')
        self.input_address.grid(row=3,column=1, padx=10, pady=10)

        self.input_contact_text = Label(self.dataframe,text='Contact',font='Nunito 20')
        self.input_contact_text.grid(row=3,column=2, padx=10, pady=10)
        self.input_contact = Entry(self.dataframe, font='Nuntio 16')
        self.input_contact.grid(row=3,column=3, padx=10, pady=10)

        self.input_education_text = Label(self.dataframe,text='Education',font='Nunito 20')
        self.input_education_text.grid(row=4,column=0, padx=10, pady=10)
        self.input_education = Entry(self.dataframe, font='Nunito 16')
        self.input_education.grid(row=4,column=1, padx=10, pady=10)

        self.input_work_text = Label(self.dataframe,text='Work (if any)',font='Nunito 20')
        self.input_work_text.grid(row=4,column=2, padx=10, pady=10)
        self.input_work = Entry(self.dataframe, font='Nunito 16')
        self.input_work.grid(row=4,column=3, padx=10, pady=10)

        self.input_remarks_text = Label(self.dataframe,text='Remarks',font='Nunito 20')
        self.input_remarks_text.grid(row=5,column=0, padx=10, pady=10)
        self.remark_val = StringVar()
        self.input_remark = Entry(self.dataframe, font='Nunito 16')
        self.input_remark.grid(row=5,column=1,padx=10,pady=10)

        self.button_red = Button(self.dataframe, text='Update',command=self.updateinfo, font='Nunito 16',width=100)
        self.button_red.grid(row=6,columnspan=4)

    def entry_data(self,event):
        self.tree_view_items = self.account_view.selection()
        self.result = self.account_view.item(self.tree_view_items,'values')
        self.account_id = self.account_view.item(self.tree_view_items,'text')
        
        self.input_first_name.delete('0','end')
        self.input_last_name.delete('0','end')
        self.input_fathersname.delete('0','end')
        self.input_mothersname.delete('0','end')
        self.input_age.delete('0','end')
        self.input_citizenshipnumber.delete('0','end')
        self.input_address.delete('0','end')
        self.input_contact.delete('0','end')
        self.input_education.delete('0','end')
        self.input_work.delete('0','end')
        self.input_remark.config(state='normal')
        self.input_remark.delete('0','end')
        # self.input_remark.config(state='normal')

        self.input_first_name.insert(0,self.result[0])
        self.input_last_name.insert(0, self.result[1])
        self.input_fathersname.insert(0,self.result[2])
        self.input_mothersname.insert(0,self.result[3])
        self.input_age.insert(0,self.result[4])
        self.input_citizenshipnumber.insert(0,self.result[5])
        self.input_address.insert(0,self.result[6])
        self.input_contact.insert(0,self.result[7])
        self.input_education.insert(0,self.result[8])
        self.input_work.insert(0,self.result[9])
        self.input_remark.insert(0, self.result[10])
        self.input_remark.config(state='disabled')

    def updateinfo(self):
        sql_names = ['First_Name', 'Last_Name', 'Fathers_Name', 'Mothers_Name', 'Age', 'Citizenship_Number', 'Location', 'Contact', 'Education', 'Work']
        new_values = [self.input_first_name.get(),self.input_last_name.get(),
        self.input_fathersname.get(),self.input_mothersname.get(),
        self.input_age.get(),self.input_citizenshipnumber.get(),
        self.input_address.get(),self.input_contact.get(),
        self.input_education.get(),self.input_work.get()]
        old_values = self.result[0:-1]

        if list(new_values) == list(old_values):
            messagebox.showinfo('Dear User','Everything is same')
            return False
        updated_values = []

        for i in range(len(old_values)):
            if old_values[i] != new_values[i]:
                updated_values.append({sql_names[i]: new_values[i]})
        
        resp = Account_manager().update_pending_acc(updated_values,self.account_id)

        if resp:
            messagebox.showinfo('Success','Updated Successfully')
            
            # Pointing the self.result to the new_values so that on next update it compares it with
            # the new values instead of the old fetched value.
            self.result = new_values

        else:
            messagebox.showerror('Error','Somthing went wrong')
