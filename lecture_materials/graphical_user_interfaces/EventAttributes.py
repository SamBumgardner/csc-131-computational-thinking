"""
File: EventAttributes.py

"""
from tkinter import *

class MouseKeyEventDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Event Demo")
        self.grid()
        canvas = Canvas(self, bg = "white", width = 200, height = 100)
        canvas.grid()
        
        # Bind with <Button-1> event
        canvas.bind("<Button-1>", self.processMouseEvent)
        
        # Bind with <Key> event
        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set() # Set canvas in focus

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)
    
    def processKeyEvent(self, event):    
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)

def main():
    """Instantiate and pop up the window."""
    MouseKeyEventDemo().mainloop()

main()
