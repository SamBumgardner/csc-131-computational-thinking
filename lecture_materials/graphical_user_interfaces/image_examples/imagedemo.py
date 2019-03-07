"""
File: imagedemo.py

Displays an image in a window.
"""

from tkinter import *

class ImageDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Image Demo")
        self.master["bg"]="green"
        self["bg"] = "blue"
        self.grid()
        self._image = PhotoImage(file = "smokey.gif")
        self._imageLabel = Label(self, image = self._image)
        self._imageLabel.grid()
        self._textLabel = Label(self, text = "Smokey the cat")
        self._textLabel.grid()

def main():
    """Instantiate and pop up the window."""
    ImageDemo().mainloop()

main()
