#!/usr/bin/python3
class Square():
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """
        Initialize instance of a Square.
        """
        self._Square__size = size

    @property
    def size(self):
        """Return size of Square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if isinstance(value, int):
            if value >= 0:
                self._Square__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area"""
        return self._Square__size ** 2

    def my_print(self):
        """Print the size of the Square."""
        if self._Square__size == 0:
            print()
            return
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end="")
            print()
