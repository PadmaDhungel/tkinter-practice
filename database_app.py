from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:
    #Class Fields
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


root = Tk()
studDB = StudentDB(root)

root.mainloop()
