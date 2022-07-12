from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('My Clock')
def gettime():
    t=strftime('%H : %M : %S %p')
    label.config(text=t)
    label.after(1000,gettime)
label=Label(root,font=('ds-digital',80),background='black',foreground='green')
label.pack(anchor='center')
gettime()
root.mainloop()