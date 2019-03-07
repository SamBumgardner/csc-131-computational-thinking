"""
File: EnlargeShrinkCircle.py
Program draws a circle on the canvas. The circle radius is increased
with a left mouse click and decreased with a right mouse click 
"""
from tkinter import *

class EnlargeShrinkCircle(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Control Circle Demo")
        self.grid()
        
        self.radius = 50
    
        self.canvas = Canvas(self, bg = "white", 
            width = 200, height = 200)
        self.canvas.grid()
        
        # Create a circle with center at (100, 100)
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius, 
            100 + self.radius, 100 + self.radius, tags = "oval")
        
        # Bind canvas with mouse events
        self.canvas.bind("<Button-1>", self.increaseCircle)
        self.canvas.bind("<Button-3>", self.decreaseCircle)
        
    def increaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius < 100:
            self.radius += 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius, 
            100 + self.radius, 100 + self.radius, tags = "oval")
        
    def decreaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -= 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius, 
            100 + self.radius, 100 + self.radius, tags = "oval")

def main():
    """Instantiate and pop up the window."""
    EnlargeShrinkCircle().mainloop()

main()
