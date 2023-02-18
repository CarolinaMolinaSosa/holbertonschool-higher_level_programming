#!/usr/bin/python3
"""Second class rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    KV_dict = {'id': 'id', 'width': '_Rectangle__width',
               'height': '_Rectangle__height',
               'x': '_Rectangle__x', 'y': '_Rectangle__y'}

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """
        update
        """
        key_list = ['id', '_Rectangle__width', '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        KV_dict = {'id': 'id', 'width': '_Rectangle__width',
                   'height': '_Rectangle__height',
                   'x': '_Rectangle__x', 'y': '_Rectangle__y'}
        for idx, el in enumerate(args):
            self.__dict__[key_list[idx]] = el
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__dict__[KV_dict[key]] = val

    def __str__(self):
        """
        __str__
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def area(self):
        """
        public_method area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        public method display self prints in stdout #
        """
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)