"""
File: CheckButton2.py

"""

from tkinter import *

def processCheckbutton():
    print("Checkbutton clicked value is", var.get())
    
root = Tk()

var = StringVar(value="Off") 
cb = Checkbutton(root, text="Check Me", variable=var, 
        onvalue="On", offvalue="Off", command = processCheckbutton)
cb.grid()
    
root.mainloop()

