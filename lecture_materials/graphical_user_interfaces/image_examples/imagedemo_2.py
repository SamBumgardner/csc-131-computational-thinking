"""
File: imagedemo.py

Displays an image in a window.
"""

from tkinter import *

class ImageDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self, bg ="blue")
        self.master.title("Image Demo")
        #self.master.rowconfigure(0, weight=1)
        #self.master.columnconfigure(0, weight=1)
        self.grid()
        #self.grid(sticky=E+W+N+S)
        self.master["bg"]="green"
        self["bg"]="blue"
        self._image = PhotoImage(file = "smokey.gif")
        self._imageLabel = Label(self, image = self._image)
        self._imageLabel.grid() #sticky=E+W+N+S
        self._textLabel = Label(self, text = "Smokey the cat", bg ="#FFFF00",
                                 fg = "red")
        #self._textLabel.grid(sticky=E+W+N+S, padx = 20, pady = 10, ipadx = 20, ipady = 10)
        self._textLabel.grid()
        #self.rowconfigure(0, weight = 1)
        #self.rowconfigure(1, weight = 1)
        #self.columnconfigure(0, weight = 1)

def main():
    """Instantiate and pop up the window."""
    ImageDemo().mainloop()

main()
