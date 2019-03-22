'''
Class to logically represent a surface that may have shapes drawn on it.
Created by: Sam Bumgardner
'''

class DrawingSurface(object):
    '''Represents a surface that may have shapes drawn on it.
    Intended to contain instances DrawableShape class.'''

    def __init__(self):
        '''Initializes a blank drawing surface.'''
        self._shapeStack = []

    def addShape(self, drawableShape):
        '''Adds a shape to the top of the stack of shapes.
        
        Positional arguments:
        drawableShape -- instance of the DrawableShape class to add.'''
        self._shapeStack.append(drawableShape)

    def popShape(self):
        '''Removes and returns the top shape of the stack.'''
        return self._shapeStack.pop()

    def getShapeById(self, requestedId):
        '''Returns the first shape found (starting from the bottom of the stack)
        that has the requested ID.'''
        for drawableShape in self._shapeStack:
            if requestedId == drawableShape.getId():
                return drawableShape

    def getShapeStack(self):
        '''Returns a copy the current shape stack.'''
        return list(self._shapeStack)

    def clearSurface(self):
        '''Removes all shapes from the DrawingSurface.'''
        self._shapeStack = []


