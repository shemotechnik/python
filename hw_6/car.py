"""
создайте класс `Car`, наследник `Vehicle`
"""
from Classworks.hw_6 import base 

class Car(base.Vehicle):
    def set_engine(self, cls):
        self.engine = cls


