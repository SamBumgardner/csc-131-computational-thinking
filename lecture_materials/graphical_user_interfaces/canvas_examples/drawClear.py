"""
File: drawClear.py 

Adds code to draw.py to allow clearing of canvas. Clicking the left mouse button
while pressing the Control key clears the canvas
"""
from tkinter import *

class Draw(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Drawing Program")
        self.grid()

        self.canvas = Canvas(self, height=100, width=150) 
        self.canvas.grid(row = 0, column = 0)

        self.oldx, self.oldy = 0, 0   # mouse coordinates 

        # bind left mouse button click event to instance method begin()
        self.canvas.bind("<Button-1>", self.begin)

        # bind mouse motion while pressing left button event to method draw()
        self.canvas.bind("<Button1-Motion>", self.draw)

        # bind Ctrl-Left button mouse click to method delete()
        self.canvas.bind('<Shift-Control-Button-1>', self.delete)

    def begin(self, event):
        'initializes the start of the curve to mouse position'
        self.oldx, self.oldy = event.x, event.y 

    def draw(self, event):
        'draws a line segment from old mouse position to new one'
        newx, newy = event.x, event.y  # new mouse position

        # connect previous mouse position to current one (identify drawn line)
        self.canvas.create_line(self.oldx, self.oldy, newx, newy,
                                tags = "segment")

        self.oldx, self.oldy = newx, newy    # new position becomes previous

    def delete(self, event):
        'clears the canvas drawn'
        self.canvas.delete("segment")


def main():
    Draw().mainloop()

main()
