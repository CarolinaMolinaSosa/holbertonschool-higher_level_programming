#!/usr/bin/python3
""""
 A class MyList that inherits from list
"""


class MyList(list):
    """Prints the list, but sorted"""

    def print_sorted(self):
        print(sorted(self))
