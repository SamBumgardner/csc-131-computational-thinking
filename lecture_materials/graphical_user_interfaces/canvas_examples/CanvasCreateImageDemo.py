"""
File: CanvasCreateImageDemo.py
"""

from tkinter import * # Import tkinter

window = Tk()
window.title("Image on Canvas") # set title
# create the canvas, size in pixels
canvas = Canvas(window, width = 400, height = 400, bg = "white") 

# grid the canvas
canvas.grid()
 
# load the .gif image file
image1 = PhotoImage(file = 'smokey.gif')
canvas.create_oval(195,195,205,205, fill="black")
 
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=200 y=200
canvas.create_image(200, 200, image = image1, anchor = E)
 
# run it ...
window.mainloop()
