from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)

labelText = StringVar()

label = Label(frame,textvariable=labelText)
button = Button(frame,text="Click me")

labelText.set('i am a labell')

label.pack()
button.pack()
frame.pack()

root.mainloop()
