from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:
    #Class Fields
    db_conn = 0
    theCursor = 0
    curr_student = 0



    def setup_db(self):

        #open or create a db
        self.db_conn = sqlite.connect('student.db')

        #Create Cursor
        self.theCursor = self.db_conn.cursor()

        try:

            #Create the table if it doesn't exist
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL);")
            self.db_conn.commit()

        except sqlite.OperationalError:
            print('Table not created, there was an error')


    def stud_submit(self):
        # Insert the student into the database
        self.db_conn.execute('INSERT INTO Students(FName,LName)'+"VALUES ('"+self.fn_entry_value.get()+"', '"+self.ln_entry_value.get()+"')")

        # clear entry boxes
        self.fn_entry.delete(0,"end")
        self.ln_entry.delete(0,"end")

        # Update listbox
        self.update_listbox()

    def update_listbox(self):
        # Delete items in List Box
        self.list_box.delete(0,END)

        # get the students from the database
        try:
            result = self.theCursor.execute("SELECT ID,FName,LName FROM Students")
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]
            #  put students in the list box
            self.list_box.insert(stud_id,stud_fname+' '+stud_lname)

        except sqlite.OperationalError:
            print('table doesnt exist')
        except:
            print('coudnt retrieve data')



    def load_student(self):
        #get the 

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
