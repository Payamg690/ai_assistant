# This starts our Rectangle class definition
class Rectangle:
    # The __init__ function is used to initialize the properties of an object
    def __init__(self, length, width):
        self.length = length  # Here we set the length property of our instance
        self.width = width  # Here we set the width property of our instance

    # This function return area of the rectangle
    def area(self):
        return self.length * self.width  # just multiply the length and the width to get the area


# This starts our Circle class definition
class Circle:
    """
    Initialize a Circle object with a given radius
    :param radius: The radius of the circle.
    :type radius: float
    """
    # The __init__ function is used to initialize the properties of an object
    def __init__(self, radius):
        self.radius = radius  # Here we set the radius property of our instance

    # This function return area of the circle
    def area(self):
        return 3.14 * self.radius * self.radius  # to find an area of a circle multiple pi (3.14) with radius squared