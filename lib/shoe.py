#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    pass