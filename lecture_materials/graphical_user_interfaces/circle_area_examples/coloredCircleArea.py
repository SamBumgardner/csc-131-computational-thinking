"""
File: coloredCircleArea.py

Set the background color for the frame and the labels
Inputs a radius of a circle and outputs its area.
"""

from tkinter import *
import math

class CircleArea(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self, bg = 'red')
        self.master.title("Circle Area") 
        self.grid()

        # Label and field for the radius
        self._radiusLabel = Label(self, text = "Radius",
                                  borderwidth = 3, relief = RAISED, bg = "yellow")
        self._radiusLabel.grid(row = 0, column = 0)
        self._radiusVar = DoubleVar()
        self._radiusEntry = Entry(self,
                                  textvariable = self._radiusVar)
        self._radiusEntry.grid(row = 0, column = 1)

        # Label and field for the area
        self._areaLabel = Label(self, text = "Area"
                                ,borderwidth = 3, relief = RAISED, fg = "#00ff00")
        self._areaLabel.grid(row = 1, column = 0, ipadx = 5, ipady = 7, padx = 5, pady = 5)
        self._areaVar = DoubleVar()
        self._areaEntry = Entry(self,
                                textvariable = self._areaVar)
        self._areaEntry.grid(row = 1, column = 1)

        # The command buton
        self._button = Button(self,
                              text = "Compute",
                              command = self._area, background = "#FF00FF")
        self._button.grid(row = 2, column = 0, columnspan = 2)

    def _area(self):
        """Event handler for the button."""
        radius = self._radiusVar.get()
        area = radius ** 2 * math.pi
        self._areaVar.set(area)

def main():
    """Instantiate and pop up the window."""
    CircleArea().mainloop()

main()
