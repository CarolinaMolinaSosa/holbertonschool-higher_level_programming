#!/usr/bin/python3
""""
Function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """return a list"""

    return (dir(obj))
