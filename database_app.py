from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:
    #Class Fields
    db_conn = 0
    theCursor = 0
    curr_student = 0



    def setup_db(self):
        print('setup database')

    def stud_submit(self):
        print('submit student')

    def update_listbox(self):
        print('update listbox')

    def load_student(self):
        print('load student')

    def update_student(self):
        print('update student')

    def __init__(self,root):
        root.title("Student Database")
        root.geometry('300x350')

        # .... 1st row .....
        fn_label = Label(root,text="First Name")
        fn_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.fn_entry_value = StringVar(root,value="")
        self.fn_entry = ttk.Entry(root,textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # .... 2nd row .....
        ln_label = Label(root,text="Lasr Name")
        ln_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        self.ln_entry_value = StringVar(root,value="")
        self.ln_entry = ttk.Entry(root,textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #..... 3rd row ......
        self.submit_button = ttk.Button(root,text="Submit",command=lambda: self.stud_submit())
        self.submit_button.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        self.update_button = ttk.Button(root,text="Update",command=lambda: self.stud_update())
        self.update_button.grid(row=2,column=1,padx=10,pady=10)

        #..... 4th row ......
        scrollbar = Scrollbar(root)
        self.list_box = Listbox(root)
        self.list_box.bind('<<listboxSelect>>',self.load_student)
        self.list_box.insert(1,"Students Here")
        self.list_box.grid(row=3,column=0,columnspan=4,padx=10,pady=10,sticky=W+E)
        self.setup_db()
        self.update_listbox()



root = Tk()
studDB = StudentDB(root)

root.mainloop()
