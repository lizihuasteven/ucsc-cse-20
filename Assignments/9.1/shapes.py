'''
Student Name: Zihua Li
Assignment 9.1: Shapes
This script creates classes representing different shapes and will implement common methods
with different implementations based on the shape.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

class Shape:
    # constructor
    def __init__(self, identifier):
        # store identifier
        self.__store_id = identifier

    def get_area(self):
        # no area calculation for this class
        print("The area cannot be calculated.")
        return None

    def get_perimeter(self):
        # no perimeter calculation for this class
        print("The perimeter cannot be calculated.")
        return None

    def get_id(self):
        # returning identifier
        return self.__store_id

class Ellipse(Shape):
    # constructor
    def __init__(self, identifier, major_axis_radius, minor_axis_radius):
        # inheriting Shape class attributes
        super().__init__(identifier)
        # storing major and minor axis radius
        self.__store_major_axis_radius = float(major_axis_radius)
        self.__store_minor_axis_radius = float(minor_axis_radius)

    def get_perimeter(self):
        # no perimeter calculation for this class
        print("The perimeter cannot be calculated.")
        return None

    def get_area(self):
        # importing math for pi
        import math
        # calculating and storing the area
        self.__area = self.__store_minor_axis_radius * self.__store_major_axis_radius * math.pi
        # returning the area
        return self.__area

class Circle(Ellipse):
    # constructor
    def __init__(self, identifier, radius):
        # inheriting Ellipse class attributes
        super().__init__(identifier, radius, radius)
        # storing radius
        self.__store_radius = float(radius)

    def get_perimeter(self):
        # importing math for pi
        import math
        # calculating and storing perimeter
        self.__perimeter = self.__store_radius * 2 * math.pi
        # returning perimeter
        return self.__perimeter

class Rectangle(Shape):
    # constructor
    def __init__(self, identifier, width, length):
        # inheriting Shape class attributes
        super().__init__(identifier)
        # storing width and length for further calculations
        self.__store_width = float(width)
        self.__store_length = float(length)

    def get_area(self):
        # calculating and storing area
        self.__area = self.__store_length * self.__store_width
        # returning the area
        return self.__area

    def get_perimeter(self):
        # calculating and storing perimeter
        self.__perimeter = self.__store_length * 2 + self.__store_width * 2
        # returning the perimeter
        return self.__perimeter

class Square(Rectangle):
    # constructor
    def __init__(self, identifier, side_length):
        # inheriting Rectangle class attributes
        super().__init__(identifier, side_length, side_length)
