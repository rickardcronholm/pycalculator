import numpy as np


class Calculator():

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def multiple(self, x, y):
        return np.multiply(x, y)

    def devide(self, x, y):
        return x/y
