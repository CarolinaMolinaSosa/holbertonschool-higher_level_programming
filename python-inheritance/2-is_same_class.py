#!/usr/bin/pythin3
""""
Function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """"returns the same object of a"""
    return type(obj) is a_class
