from tkinter import *
from datetime import *
import tkinter.messagebox as msg
from tkinter import filedialog,simpledialog
ar=Tk()
def new():
    global file
    if len(textarea.get('1.0', END + '-1c')) > 0:
        if msg.askyesno("Notepad", "Do you want to save changes?"):
            save()
        else:
            textarea.delete(0.0, END)
    ar.title("Notepad")
def openn():
    fd = filedialog.askopenfile(parent=ar, mode='r')
    t = fd.read()
    textarea.delete(0.0, END)
    textarea.insert(0.0, t)
def save():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd != None:
        data = textarea.get('1.0', END)
    fd.write(data)
    ar.title("Notepad-By VSHarshaS")

def saveas():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = textarea.get(0.0, END)
    fd.write(t.rstrip())
    ar.title("Notepad-By VSHarshaS")


def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def selectall():
    textarea.event_generate(("<<SelectAll>>"))
def dt():
    s=datetime.today()
    msg.showinfo("Date and Time are",s)
def about():
    msg.showinfo("About this notepad","THIS NOTEPAD IS MADE BY VSHARSHAS")
def clearall():
    textarea.delete(0.0, END)



ar.wm_iconbitmap("notepad.ico")
ar.title("Untitled Notepad-By VSHarshaS")
ar.geometry("500x500")
textarea = Text(ar, font="lucida 13")
file = None
textarea.pack(expand=True, fill=BOTH)

scrollbar=Scrollbar(textarea)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)


menu=Menu(ar)
filemenu=Menu(menu,tearoff=0)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=openn)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Save As",command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editmenu=Menu(menu,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_separator()
editmenu.add_command(label="Time/Date",command=dt)
editmenu.add_command(label="Select All",command=selectall)
editmenu.add_separator()
editmenu.add_command(label="Clear All",command=clearall)


helpmenu=Menu(menu,tearoff=0)
helpmenu.add_command(label="About",command=about)

menu.add_cascade(label="File",menu=filemenu)
menu.add_cascade(label="Edit",menu=editmenu)
menu.add_cascade(label="Help",menu=helpmenu)
ar.config(menu=menu)

ar.mainloop()