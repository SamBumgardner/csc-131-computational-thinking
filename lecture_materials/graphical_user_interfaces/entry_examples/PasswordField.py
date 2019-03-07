"""
File: PasswordField.py

"""
from tkinter import *

class PasswordField(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Password Field")
        self.grid()

        # Label and field for the password
        self._passLabel = Label(self, text = "Enter password")
        self._passLabel.grid(row = 0, column = 0)
        
        self._passVar = StringVar()
        self._passEntry = Entry(self, textvariable = self._passVar, show ="*")
        self._passEntry.grid(row = 0, column = 1)

        # The command buton
        self._button = Button(self, text = "Process",
                              command = self._process)
        self._button.grid(row = 1, column = 0, columnspan = 2)

    def _process(self):
        """Event handler for the button."""
        print(self._passVar.get())

def main():
    """Instantiate and pop up the window."""
    PasswordField().mainloop()

main()

