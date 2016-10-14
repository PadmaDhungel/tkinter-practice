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

text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print('font picked: ',text_font.get())

font_menu = Menu(the_menu,tearoff=0)

font_menu.add_radiobutton(label="Times",variable=text_font,command=change_font)


view_menu = Menu(the_menu,tearoff=0)

line_numbers = IntVar()
line_numbers.set(1)

view_menu.add_checkbutton(label="Line Numbers",variable = line_numbers)

view_menu.add_cascade(label="fonts",menu=font_menu)

the_menu.add_cascade(label="view",menu=view_menu)


help_menu = Menu(the_menu,tearoff=0)

help_menu.add_command(label="About",accelerator="Command-A",command=show_about)

the_menu.add_cascade(label="help",menu=help_menu)

root.bind('<Command-A>',show_about)
root.bind('<Command-a>',show_about)



root.config(menu=the_menu)


root.mainloop()
