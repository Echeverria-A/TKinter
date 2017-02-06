
from Tkinter import *
import time
from PIL import Image, ImageTk
import tkMessageBox

root = Tk()
root.title("Alarm Clock")
root.configure(background='white')




def alarm():
   tkMessageBox.showinfo("Alarm", "Alarm Reached!")

def getText():
    global myTime
    myString = inputBox.get()



#clock
time1 = ''
clock = Label(root, font=('Times New Roman',30, 'bold',), bg='#f282db')
clock.grid(row=1, column=0, sticky=EW, columnspan=6)
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)




    


#menubar        
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Save")
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
 
#buttons
button1 = Button(root, text="Hour",)
button1.grid(row=3, column=0)

button4 = Button(root, text="Minute",)
button4.grid(row=3, column=3)

button4 = Button(root, text="Set Alarm",)
button4.grid(row=4, column=1 , columnspan=2)






#Up button image
image = Image.open("up.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

button2= Button(root, text="B", image=photo)
button2.image = photo
button2.grid(row=3, column=1,)

#down button image
image = Image.open("down.png")
image = image.resize((21,25,))
photo = ImageTk.PhotoImage(image)

button3= Button(root, text="B", image=photo)
button3.image = photo
button3.grid(row=3, column=2,)


#Entry Box Text
#w=Entry(root, bg="white")
#w.grid(row=5,column=1)
#button5=Button(root, text="Set Alarm", command=getText)
#button5.grid(row=5,column=2)






 
 
 
 
 
tick()
root.mainloop(  )

