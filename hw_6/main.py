# -*- coding: utf-8 -*-
""" 
Created on Fri Mar  7 13:53:26 2025

@author: nurul
"""
from Classworks.hw_6 import base, engine, car, plane

vh = base.Vehicle(50,50,10)
vh.start()
vh.move(2)

new_plane = plane.Plane(10, 50)
new_plane.load_cargo(10)
print(new_plane.cargo)

new_plane.load_cargo(20)
print(new_plane.cargo)

new_plane.remove_all_cargo()
print(new_plane.cargo)


new_engine = engine.Engine("New Engine", 10)
new_car = car.Car(vh)
new_car.set_engine(new_engine)
print(new_car.engine)

