#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: private size """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int. """

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size != 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

	@property
	def position(self):
	   """Get/set the current position of the square."""
	   return (self.__position)

	@position.setter
	   def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

	 [print("") for i in range(0, self.__position[1])]
	 for i in range(0, self.__size):
 	     [print(" ", end="") for j in range(0, self.__position[0])]
             [print("#", end="") for k in range(0, self.__size)]
             print("")
