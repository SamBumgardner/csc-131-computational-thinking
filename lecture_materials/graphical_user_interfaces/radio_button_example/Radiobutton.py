'''
RadioButton.py

A demo of radio buttons
'''
from tkinter import *

class RadioButton(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Radio Buttons")
        self.grid()

        frame1 = Frame(self) # pane to contain radio buttons
        frame1.grid()
        
        self.v1 = IntVar(value=2)
        
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                            variable = self.v1, value = 1,
                            command = self.processRadiobutton)
        rbRed.grid(row = 0, column = 0)

        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow",
                               variable = self.v1, value = 2,
                               command = self.processRadiobutton)
        rbYellow.grid(row = 0, column = 1)

    def processRadiobutton(self):
        print(("Red" if self.v1.get() == 1 else "Yellow")
            + " is selected " )

def main():
    RadioButton().mainloop()

main()
