"""
File: AnimationDemo.py

"""
from tkinter import *

class AnimationDemo(Frame): 
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Animation Demo") # Set a title 
        self.grid()
        
        width = 250 # Width of the canvas
        canvas = Canvas(self, bg = "white", width = 250, height = 50)
        canvas.grid()
        
        x = 0 # Starting x position
        canvas.create_text(x, 30, text = "Message moving?", tags = "text", anchor = W)
        
        dx = 1
        while True:
            try:
                if x < width:
                    # Move text dx unit
                    x += dx  # Get the current position for string
                    canvas.move("text", dx, 0)
                else:
                    x = 0 # Reset string position to the beginning
                    canvas.move("text", -width, 0) 
                canvas.after(15) # Sleep for 15 milliseconds
                canvas.update() # Update canvas
            except:
                break
                

def main():
    """Instantiate and pop up the window."""
    AnimationDemo().mainloop()  # Create an event loop

main()

