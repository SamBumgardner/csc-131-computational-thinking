'''
Simple class that contains basic information about a shape that can be drawn on a canvas.
Created by: Sam Bumgardner
'''

class DrawableShape(object):
    '''Stores (and provides access to) basic information about a shape.'''
    RECTANGLE_TYPE = "rectangle"
    OVAL_TYPE = "oval"
    
    _NEXT_ID = "0"
    
    def __init__(self, type, coords, fillColor=None, id=None):
        '''Initializes instance variables.
            
        Positional arguments:
        self -- instance of DrawableShape that is being instantiated.
        type -- string describing the type of shape. 
            Expected to be one of the values designated in the *_TYPE class variables.
        coords -- list of tuples that each represent an (x, y) coordinate pair.
            Only the coordinates necessary to draw the shape should be provided.
        
        Optional Keyword arguments:
        fillColor -- string representing fill color used by a shape. 
            Expected to be a hexidecimal representation (0xFF00FF) or
            the common name of a color like 'red'. No value means no fill is desired.
        id -- string identifier that is unique among DrawableShapes.
            If no value is provided, the class will automatically provide 
            a value that is unique among other automatically generated IDs.
            NOTE: id generation is NOT thread-safe (not that it matters for our class).
        '''
        self._type = type
        self._coords = coords
        self._fillColor = fillColor

        if (id == None):
            self._id = DrawableShape._NEXT_ID
            DrawableShape._NEXT_ID = str(int(DrawableShape._NEXT_ID) + 1)

    def getShapeType(self):
        '''Returns the type of shape as a string.'''
        return self._type

    def getCoordinates(self):
        '''Returns the shape's (x,y) coordinates as a list of tuples.'''
        return self._coords

    def getFillColor(self):
        '''Returns the fill color of the shape as a string.
        A value of None means the shape has no fill whatsoever.'''
        return self._fillColor

    def getId(self):
        '''Returns the shape's ID as a string.'''
        return self._id

