from abc import ABC
from Classworks.hw_6 import exceptions

class Vehicle(ABC):
    def __init__(self, weight = 50, fuel = 0, fuel_consumption = 10, max_cargo = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True 
            else:
                raise exceptions.LowFuelError
            
    def move(self, distanation = 0):
        if self.started:
            if self.fuel < distanation * self.fuel_consumption:
                raise exceptions.NotEnoughFuel
            else:
                self.fuel -= distanation * self.fuel_consumption
        else:
            raise exceptions.NotStartedError
    
    @property
    def max_cargo(self):
        return self.__max_cargo

    @max_cargo.setter
    def max_cargo(self, max_cargo):
        self.__max_cargo = max_cargo