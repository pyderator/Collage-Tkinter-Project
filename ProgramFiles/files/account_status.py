from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from MergeSort import MergeSort

class Show_Account:

    def __init__(self, root):
        self.root = root
        self.root.title('Account View')

        self.tree_view_frame = Frame(self.root)
        self.tree_view_frame.pack(fill=X)

    def show_view(self, arr):
        scroll_x1 = Scrollbar(self.tree_view_frame, orient=HORIZONTAL)
        scroll_y1 = Scrollbar(self.tree_view_frame, orient=VERTICAL)

        #Inactive Students Tree View

        self.account_view = ttk.Treeview(self.tree_view_frame, selectmode='browse', columns=(
            'Account Id', 'Created Date', 'Credit Amount', 'Debit Amount'),
                                          xscrollcommand=scroll_x1.set, yscrollcommand=scroll_y1.set)
        scroll_x1.pack(side=BOTTOM, fill=X)
        scroll_y1.pack(side=RIGHT, fill=Y)
        scroll_x1.config(command=self.account_view.xview)
        scroll_y1.config(command=self.account_view.yview)
        self.account_view.heading('Account Id', text="Account Id")
        self.account_view.heading('Created Date', text="Created Date")
        self.account_view.heading('Credit Amount', text="Credit Amount")
        self.account_view.heading('Debit Amount', text="Debit Amount")
        self.account_view['show'] = 'headings'
        self.account_view.column('Account Id', width=300, anchor='center')
        self.account_view.column('Created Date', width=200, anchor='center')
        self.account_view.column('Credit Amount', width=200, anchor='center')
        self.account_view.column('Debit Amount', width=200, anchor='center')
        self.account_view.pack(fill=BOTH, expand=1)

        sorted_arr = MergeSort().divide_array(arr)
        
        for i in sorted_arr:
            self.account_view.insert('','end', text=i[0], values=(i[1],i[2], i[3],i[4]))
