from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from datetime import datetime
from threading import *

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Lmao", entrytxt)
    
def addtolist():
    entrytxt = entry1.get()
    listbox1.insert(END,entrytxt)
    entry1.delete(0,END)

def addtolist2(event):
    entrytxt = entry1.get()
    listbox1.insert(END,entrytxt)
    entry1.delete(0,END)
    
def clearlist(event):
    listbox1.delete(0,END)

def c4d():
    names = listbox1.get(0,END)
    if entry.get() in names:
        return True
    else:
        return False

def openfileR():
    print "Open File R"
    
def openfileW():
    f = open("ReadMePlz.txt", 'w')
    names = listbox1.get(0,END)
    for i in names:
        f.write(i+"\n")
    
    f.close()
    
d=datetime.now()
y = d.year
h=d.hour

def generate():
    while(1):
        print "Hello"
    
thread1=Thread(target=generate)
#thread1.start()
    
    

    




root = Tk() #gives us a blank canvas object to work with
root.title("We Up In 'Ere BOYZ")

button1 = Button(root, text="Press 2 get lit", command=c4d)
button1.grid(row=1, column=1)

entry1= Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="WE OUTCHEA", bg="magenta",)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)
listbox1.bind("<Button-3>", clearlist)


listbox1.insert(END,"WE")
listbox1.insert(END,"EATIN")
listbox1.insert(END,"BoYZ")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)














mainloop() #causes the windows to display on the screen until program closes