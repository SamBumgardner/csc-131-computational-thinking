"""
File: CheckButton1.py

"""

from tkinter import *

def processCheckbutton():
    print("Checkbutton clicked value is", var.get())
    
root = Tk()
root.title("Check Button")
 
var = IntVar()
cb = Checkbutton(root, text="Check Me", variable=var,
         command = processCheckbutton)
cb.grid()



    
root.mainloop()

