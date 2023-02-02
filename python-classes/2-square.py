#!/usr/bin/python3
""""class Square that defines a square by: (based on 1-square.py)"""


class Square:

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError
            raise ValueError
        self.__size = size
