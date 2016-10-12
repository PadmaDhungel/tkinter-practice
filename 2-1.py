from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open_msg_box():
    messagebox.showwarning("TRIGGER WARNING","TRIGGER WARNING !!!!!")


root = Tk()

root.geometry("400x400+300+300")

root.resizable(width=False,height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",foreground="midnight blue",font="Times 20 bold italic",padding=20)

print(ttk.Style().theme_names())
print(style.lookup("Tbutton","font"))
print(style.lookup("Tbutton","foreground"))
print(style.lookup("Tbutton","padding"))

theButton = ttk.Button(frame,text="imp. button", command = open_msg_box)
theButton['state'] = 'disabled'
theButton['state'] = 'normal'
theButton.pack()
frame.pack()

root.mainloop()
