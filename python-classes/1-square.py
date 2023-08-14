#!/usr/bin/python3
"""This is the "square" module.
This module provides a simple Square class with intialize size.
Size defaults to 0. Raise errors on invalid inputs.
"""
class Square:
    """A  class that defines a square by size"""
    def __init__(self, Square__size=0):
        if type(Square__size) != int:
            raise TypeError("size must be an integer")
        if Square__size < 0:
            raise ValueError("size must be >= 0")
        self.__size__ = Square__size

      