from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning('About','this awesome program was made in 2016 ')

root = Tk()

the_menu = Menu(root)

file_menu = Menu(the_menu,tearoff=0)

file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()

file_menu.add_command(label="Quit",command=quit_app)

the_menu.add_cascade(label="File",menu=file_menu)

root.config(menu=the_menu)


root.mainloop()
