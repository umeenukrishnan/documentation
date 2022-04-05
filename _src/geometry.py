class circle:

    """
        This is circle class
    """

    def __init__(self, radius):
        """
        Class constructure
        """
        self.r = radius

    def perimeter(self):
        """
        This method calculates the perimeter of the circle
        """
        return 2*3.14*self.r

    def area(self):
        """
        This method calculates the area of the circle
        """
        return 3.14*self.r**2


class cylinder:

    def __init__(self, radius, height):
        """
        Class constructure
        """
        self.r = radius
        self.h = height

    def surface_are(self):
        """
        Surface area of the cylinder
        """
        return 2*3.14*self.r*(self.h+self.r)

    def volume(self):
        """
        Volume of the cylinder
        """
        return 3.14*self.h*self.r**2