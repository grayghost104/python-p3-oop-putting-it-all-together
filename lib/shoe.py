#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, 
    # condition
    ):
        self.brand = brand
        self.size = size
        self.condition = None
    
    def get_size(self):
        return self._size
    def set_size(self, value):
        if type(value) is int:
            self._size = value
        else:
            print("size must be an integer")  
    size = property(get_size, set_size)

    def cobble(self, 
    # condition
    ):
        print("Your shoe is as good as new!")
        self.condition = "New"

    # def condition(self):
    #     condition = "New"










    # @classmethod
    # def srepair(cls):
    #     for shoe in cls.all:
    #         srepair.repair()