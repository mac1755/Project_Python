import numpy as np
import matplotlib.pyplot as plt



class Cection:

    def __init__(self, a, n):
        self.name = a
        self.count = n

    def cection1(self):
        print(self.name + str(self.count))

cection = Cection("私は", 20)
cection.cection1()