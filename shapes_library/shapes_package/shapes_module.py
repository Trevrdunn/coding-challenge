import math


class Circle:
    """
    This class implements the Circle API
    """
    def __init__(self, radius: float = None):
        if radius <= 0:
            raise ValueError("Supplied radius must be > 0")
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


class Rectangle:
    """
    This class implements the Rectangle API
    """
    def __init__(self, height: float = None, width: float = None):
        self.height = height
        self.width = width
        
    def area(self):
        return round(self.height * self.width, 2)


        