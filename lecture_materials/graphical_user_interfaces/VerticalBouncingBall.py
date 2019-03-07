'''
A program to animate a vertical bouncing ball
Program Name: VerticalBouncingBall.py
'''

from tkinter import *

class Pong(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bouncing Ball")
        self.grid()
        canvas_width = 800  # canvas width
        canvas_height = 400 # canvas height 
        self.canvas = Canvas(self, width = canvas_width, height = canvas_height , bg = "white")
        self.canvas.grid()

        # draw ball near the top left corner of the canvas; top-left corner of surrounding box is at (2,2)
        ball_diameter = 20 # in pixels
        top_left_x = 2 # top-left coordinate of circle's bounding rectangle 
        top_left_y = 2
        self.canvas.create_oval(top_left_x, top_left_y, top_left_x + ball_diameter,
                                top_left_y + ball_diameter, fill = "red", tags = "ball")
        
        direction = "down" # ball's direction
        dy = 2        
        # move ball
        while True:
            # keep trak of ball's movement, update direction, and draw ball as needed
            if direction == "down":
                self.canvas.move("ball", 0, dy)
                top_left_y += dy
                if top_left_y + ball_diameter >= canvas_height: # ball has hit bottom wall
                    direction = "up"      
            else: # i.e., direction is "up"
                self.canvas.move("ball", 0, -dy)
                top_left_y -= dy
                if top_left_y <= 0: # ball has hit top wall
                    direction = "down"
                
            self.canvas.after(15) # Sleep for 15 milliseconds
            self.canvas.update() # Update canvas

def main():
    Pong().mainloop()

main()
