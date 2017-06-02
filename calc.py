from Tkinter import *
import parser
import Tkinter
import tkFileDialog
import tkMessageBox 

def Directions():
    tkMessageBox.showinfo("Directions", "Press enter or click button to compute the integer result")
def clear_all():
    display.delete(0, END)

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    whole_string = display.get()
    if len(whole_string):        
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press Clear All again")

def calculate(self):
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")
        
    
def openfileW():
    f = open("Readme.txt", 'w')
    names = display.get()
    f.write(names)
    f.close()
    
def openfileR():
    f = open("Readme.txt", "r")
    for line in f:
        name = line
        display.delete(0,END)
        display.insert(END, name)
    f.close()

def save(self):
    text_box= self.toal
    print text_box
    f= open ("ReadMe.txt.", "w")
    total =str(text_box)
    f.write(total)
    f.close()
    
def askopenfile(self):
    return tkFileDialog.askopenfile(mode='r', **self.file_opt)
i = 0

root = Tk()
root.title('TkinterCalc')
text = Text(root)
root.geometry("500x500")

for x in range(10):
  Grid.columnconfigure(root, x, weight=1)

for y in range(10):
  Grid.rowconfigure(root, y, weight=1)


display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky=N+S+E+W)

button1 = Button(root, text = "1", command = lambda : get_variables(1), foreground ="black")
button1.grid(row = 2, column = 0, sticky=N+S+E+W)

button2 = Button(root, text = "2", command = lambda : get_variables(2), foreground ="black")
button2.grid(row = 2, column = 1, sticky=N+S+E+W)

button3 = Button(root, text = "3", command = lambda : get_variables(3), foreground ="black")
button3.grid(row = 2, column = 2, sticky=N+S+E+W)

button4 = Button(root, text = "4", command = lambda : get_variables(4), foreground ="black")
button4.grid(row = 3 , column = 0, sticky=N+S+E+W)

button5 = Button(root, text = "5", command = lambda : get_variables(5), foreground ="black")
button5.grid(row = 3, column = 1, sticky=N+S+E+W)

button6 = Button(root, text = "6", command = lambda : get_variables(6), foreground ="black")
button6.grid(row = 3, column = 2, sticky=N+S+E+W)

button7 = Button(root, text = "7", command = lambda : get_variables(7), foreground ="black")
button7.grid(row = 4, column = 0, sticky=N+S+E+W)

button8 = Button(root, text = "8", command = lambda : get_variables(8), foreground ="black")
button8.grid(row = 4, column = 1, sticky=N+S+E+W)

button9 = Button(root , text = "9", command = lambda : get_variables(9), foreground ="black")
button9.grid(row = 4, column = 2, sticky=N+S+E+W)

zero = Button(root, text = "0", command = lambda : get_variables(0), foreground ="black")
zero.grid(row = 5, column = 0, sticky=N+S+E+W, columnspan=2)

result = Button(root, text = "=", foreground = "black")
result.grid(row = 3, column = 4, sticky = N+S, rowspan= 3)
result.bind("<Button-1>", calculate)
root.bind("<Return>", calculate)

plus = Button(root, text = "+", command =  lambda : get_operation("+"), foreground ="blue")
plus.grid(row = 2, column = 3, sticky=N+S+E+W)

minus = Button(root, text = "-", command =  lambda : get_operation("-"), foreground ="blue")
minus.grid(row = 3, column = 3, sticky=N+S+E+W)

multiply = Button(root,text = "*", command =  lambda : get_operation("*"), foreground ="blue")
multiply.grid(row = 4, column = 3, sticky=N+S+E+W)

divide = Button(root, text = "/", command = lambda :  get_operation("/"), foreground ="blue")
divide.grid(row = 5, column = 3, sticky=N+S+E+W)


percent = Button(root, text = "%", command = lambda :  get_operation("%"))
percent.grid(row = 5, column = 2, sticky=N+S+E+W)


eh = Button(root, text = "^2", command = lambda :  get_operation("**2"), foreground="blue")
eh.grid(row = 2, column = 4, sticky=N+S+E+W)



menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Directions", command=Directions)
filemenu.add_separator()

editmenu = Menu(menu)
menu.add_cascade(label="Clear", menu=editmenu)
editmenu.add_command(label="Clear", command=clear_all)

                
root.mainloop()
