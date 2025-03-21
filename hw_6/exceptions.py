"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self):
        print("Бак с топливом пуст")

class NotEnoughFuel(Exception):
    def __init__(self):
        print("Недостаточно топлива для старта")

class CargoOverload(Exception):
    def __init__(self):
        print("Перегруз")

class NotStartedError(Exception):
    def __init__(self):
        print("Сначала надо завести машину")