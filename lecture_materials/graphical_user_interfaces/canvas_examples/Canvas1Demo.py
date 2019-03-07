"""
File: Canvas1Demo.py

"""
from tkinter import *

class Canvas1Demo(Frame):

    def __init__(self): 
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Canvas Demo")
        self.grid()

        # create a canvas and place in this frame
        self.canvas = Canvas(self, width = 200, height = 100, 
            bg = "white")
        self.canvas.grid(row = 0, column = 0)

        # Place buttons in a frame
        frame = Frame(self)
        frame.grid(row = 1, column = 0)
        rectangle = Button(frame, text = "Rectangle", 
            command = self.displayRect)
        oval = Button(frame, text = "Oval", 
            command = self.displayOval)
        arc = Button(frame, text = "Arc", 
            command = self.displayArc)
        polygon = Button(frame, text = "Polygon", 
            command = self.displayPolygon)
        line = Button(frame, text = "Line", 
            command = self.displayLine)
        string = Button(frame, text = "String", 
            command = self.displayString)
        clear = Button(frame, text = "Clear", 
            command = self.clearCanvas)

        rectangle.grid(row = 0, column = 0)
        oval.grid(row = 0, column = 1)
        arc.grid(row = 0, column = 2)
        polygon.grid(row = 0, column = 3)
        line.grid(row = 0, column = 4)
        string.grid(row = 0, column = 5)
        clear.grid(row = 0, column = 6)

    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
        
    # Display an oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill = "red", 
            tags = "oval")
    
    # Display an arc
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start = 0, 
            extent = 90, width = 8, fill = "yellow", tags = "arc")
    
    # Display a polygon
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")
    
    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill = "red", 
            tags = "line")
        self.canvas.create_line(10, 90, 190, 10, width = 9, 
            arrow = "last", activefill = "blue", tags = "line")
    
    # Display a string
    def displayString(self):
        self.canvas.create_text(60, 40, text = "Hi, I am a string", 
           font = "Times 20 bold underline", tags = "string")
    
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete(ALL)

def main():
    """Instantiate and pop up the window."""
    Canvas1Demo().mainloop()

main()
