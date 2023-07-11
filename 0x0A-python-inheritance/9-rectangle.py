#!/usr/bin/python3
"""currently empty class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialize the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle

        Returns:
            rectangle's area
        """
        return self.__width * self.__height

    def __str__(self):
        """rectnagle's description

        Returns:
            info
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """represent the rectangle"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
