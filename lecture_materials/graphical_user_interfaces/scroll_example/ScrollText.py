"""
File: ScrollText.py

"""
from tkinter import *
    
class ScrollText:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Scroll Text Demo") # Set title
        
        frame1 = Frame(window) # Create a pane for Text and Scrollbar
        frame1.grid(row = 0, column = 0)
        
        scrollbar = Scrollbar(frame1, orient = HORIZONTAL)
        scrollbar.grid(row = 1, column = 0, sticky = E + W)
        text = Text(frame1, width = 10, height = 3, wrap = NONE, 
                    xscrollcommand = scrollbar.set)
        text.grid(row = 0, column = 0)
        scrollbar["command"] = text.xview
        
        window.mainloop() # Create an event loop

ScrollText()
