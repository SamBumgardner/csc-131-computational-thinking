from tkinter import *
from drawableShape import DrawableShape
from drawingSurface import DrawingSurface

class GeometricShapeGui(Frame):
    _LAST_DRAWN_NONE = 0
    _LAST_DRAWN_RECT = 1
    _LAST_DRAWN_OVAL = 2

    def __init__(self):
        """Sets up the model, window, and widgets."""
        # Create the logical drawing surface
        self._drawingSurface = DrawingSurface()
        
        # Create the window and gui elements.
        Frame.__init__(self)
        self.master.title("GUIs drawing geometric shapes")
        self.grid()
        
        # Create a canvas and place in this frame
        self._canvas = Canvas(self, width = 300, height = 300, bg = "white")
        self._canvas.grid(row = 0, column = 0)

        # Place buttons in a frame
        buttonFrame = Frame(self)
        buttonFrame.grid(row = 1, column = 0)

        # Set up shape buttons
        self._lastDrawnShape = IntVar(value=0)

        self._rectButton = Radiobutton(buttonFrame, text = "Rectangle",
            variable = self._lastDrawnShape,
            value = GeometricShapeGui._LAST_DRAWN_RECT,
            command = self._addRect)
        self._ovalButton = Radiobutton(buttonFrame, text = "Oval",
            variable = self._lastDrawnShape,
            value = GeometricShapeGui._LAST_DRAWN_OVAL,
            command = self._addOval)

        # Set up checkbox for fill
        self._fillNext = IntVar(0)
        
        self._fillCheckButton = Checkbutton(buttonFrame, text="Filled",
            variable=self._fillNext)

        # Set up button to clear canvas
        self._clearButton = Button(buttonFrame, text = "Clear",
            command = self._clear)

        self._rectButton.grid(row = 0, column = 0)
        self._ovalButton.grid(row = 0, column = 1)
        self._fillCheckButton.grid(row = 0, column = 2)
        self._clearButton.grid(row = 0, column = 3)

    def _addRect(self):
        newShape = None
        coords = [(50, 50), (250, 250)]
        
        newShape = DrawableShape(DrawableShape.RECTANGLE_TYPE, coords,
                        fillColor = "red" if self._fillNext.get() else None)
        
        self._drawingSurface.addShape(newShape)
        self._drawShapes()

    def _addOval(self):
        newShape = None
        coords = [(50, 100), (250, 200)]
        
        newShape = DrawableShape(DrawableShape.OVAL_TYPE, coords,
                        fillColor = "yellow" if self._fillNext.get() else None)
        
        self._drawingSurface.addShape(newShape)
        self._drawShapes()

    def _clear(self):
        self._lastDrawnShape.set(GeometricShapeGui._LAST_DRAWN_NONE)
        self._fillNext.set(0)
        self._drawingSurface.clearSurface()
        self._drawShapes()

    def _drawShapes(self):
        shapes = self._drawingSurface.getShapeStack()
        
        # start with a fresh canvas
        self._canvas.delete(ALL)
        
        # draw shapes onto canvas in order.
        for shape in shapes:
            coords = shape.getCoordinates()
            
            if shape.getShapeType() == DrawableShape.RECTANGLE_TYPE:
                self._canvas.create_rectangle(coords[0][0], coords[0][1],
                    coords[1][0], coords[1][1], fill = shape.getFillColor(),
                    tags = shape.getId())

            elif shape.getShapeType() == DrawableShape.OVAL_TYPE:
                self._canvas.create_oval(coords[0][0], coords[0][1],
                    coords[1][0], coords[1][1], fill = shape.getFillColor(),
                    tags = shape.getId())


def main():
    """Instantiate and pop up the window."""
    GeometricShapeGui().mainloop()

main()
