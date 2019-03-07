"""
File: fontdemo.py

Displays text with font attributes.
"""

from tkinter import *
import tkinter.font

class FontDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Font Demo")
        self.grid()
        font1 = tkinter.font.Font(family = "Verdana",
                           size = 20, slant = "italic")
        self._label = Label(self, font = font1,
                            text = "Hello world!")
        self._label.grid()
        #print(tkinter.font.families())

def main():
    """Instantiate and pop up the window."""
    FontDemo().mainloop()

main()
