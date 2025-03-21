"""
создайте класс `Plane`, наследник `Vehicle`
"""
from Classworks.hw_6 import base, exceptions


class Plane(base.Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo 
        super().__init__(max_cargo=max_cargo)
    
    def load_cargo(self, additional_cargo):
        if additional_cargo + self.cargo > super().max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo = additional_cargo
    
    def remove_all_cargo(self):
        print("Текущая грузоподъемность", self.cargo)
        self.cargo = 0
