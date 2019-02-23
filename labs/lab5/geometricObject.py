class GeometricObject(object):
    def __init__(self, color = "white", filled = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled
  
    def __str__(self):
        return "color: " + self.color + \
            " and filled: " + str(self.filled)
