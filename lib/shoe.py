#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand=None, size=0):
        self.brand = brand
        self.size = size
        self.conditoin = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            print("size must be an integer")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


stan_smith = Shoe("Addidas", 9)
stan_smith.cobble()
