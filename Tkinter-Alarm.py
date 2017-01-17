from Tkinter import *
import time
 
root = Tk()
root.title("Alarm Clock")

time1 = ''
clock = Label(root, font=('Calisto MT', 20, 'bold'), bg='pink')
clock.grid(row=2, column=3)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Save")
menubar.add_cascade(label="File", menu=filemenu)
 
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
 
tick()
root.mainloop(  )

