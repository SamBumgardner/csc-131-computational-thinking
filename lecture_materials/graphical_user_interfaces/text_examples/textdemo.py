"""
File: textdemo.py

Displays text in a multiline text area.
"""

from tkinter import *

class TextDemo(Frame):
    """Demonstrates a multiline text area."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Text Demo")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)
        self._text = "This is a long string to wrap."
        self._outputArea = Text(self,
                                width = 20,
                                height = 5,
                                wrap = WORD)
        self._outputArea.grid(row = 0, column = 0,
                              columnspan = 2,
                              sticky = W+E+N+S)
        self._showButton = Button(self,
                                  text = "Show",
                                  command = self._show)
        self._showButton.grid(row = 1, column = 0)
        self._clearButton = Button(self,
                                  text = "Clear",
                                  command = self._clear)
        self._clearButton.grid(row = 1, column = 1)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

    def _show(self):
        self._outputArea.insert("1.0", self._text)

    def _clear(self):
        self._outputArea.delete("1.0", END)

def main():
    """Instantiate and pop up the window."""
    TextDemo().mainloop()

main()
