"""
circle.py
A simple example on classes
"""

import math

class Circle(object):
    """A circle is represented by the value of its radius"""
    def __init__(self, radius = 1):
        """Initializes raduis"""
        self._radius = radius

    def __str__(self):
        """Return a string representation of a circle"""
        return 'A circle with radius ' + str(self._radius)

    def getArea(self):
        """Returns area"""
        return math.pi * self._radius * self._radius

    def getCircumference(self):
        """Returns circumference"""
        return 2 * math.pi * self._radius
    
