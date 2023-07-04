#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """set the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """area of the rectangle

        Returns:
            area = width x height
        """

        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle

        Returns:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """biggest rectangle

        Args:
            rect_1: rectangle instance
            rect_2: rectangle instance

        Returns:
            biggest rect based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """print rectangle"""
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect

        for i in range(0, self.height):
            for j in range(0, self.width):
                rect += str(self.print_symbol)
            if i < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """rectanle's representation

        Returns:
            object representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deleted ;("""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """square instance"""
        return (cls(size, size)
