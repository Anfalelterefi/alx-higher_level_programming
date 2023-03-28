Mmog12
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
alx-higher_level_programming/0x06-python-classes/3-square.py
@Mmog12
Mmog12 oop
 1 contributor
Executable File  22 lines (17 sloc)  552 Bytes
#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
