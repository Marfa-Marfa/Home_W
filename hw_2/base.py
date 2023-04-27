""""
Доработайте базовый класс base.Vehicle:
"""
from abc import ABC
from Home_W.hw_2 import exceptions
class Vehicle(ABC):
    weight: int
    fuel: int
    fuel_consumption: int
    started: bool = False

# 2.1. Добавление атрибутов weight, started, fuel, fuel_consumption со значениями по умолчанию
# 2.2. Добавление инициализатора для установки weight, fuel, fuel_consumption
    def __init__(self, weight=1000,  fuel=110, fuel_consumption=5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

# 2.3.Добавление метода start, который, если ещё не состояние started, проверяет,
# что топлива больше нуля, и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
    def start(self):
        if self.started:
            pass
        else:
            if self.fuel <= 0:
                raise exceptions.LowFuelError
            else:
                self.started = True

# 2.4.Добавление метода move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
# и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, dist: int):
        expected_fuel_to_spend = self.fuel_consumption * dist
        if self.fuel < expected_fuel_to_spend:
            raise exceptions.NotEnoughFuel(f"Not Enough Fuel! Need {expected_fuel_to_spend}, but have only {self.fuel}")

        else:
            self.fuel -= expected_fuel_to_spend
            print(f'Drive distance {dist}, spent {expected_fuel_to_spend}, left {self.fuel}')


#Отладка сценария через __name__ с помощью интерактивного сеанса Python
if __name__ == '__main__':
    vehicle = Vehicle(weight=1000, fuel=110, fuel_consumption=5) # Cоздание объекта класса Vehicle
    vehicle.move(dist=10) # вызов метода
    print("left =", vehicle.fuel)
