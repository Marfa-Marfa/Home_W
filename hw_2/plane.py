"""
создайте класс `Plane`, наследник `Vehicle`
"""

from Home_W.hw_2.base import Vehicle
from Home_W.hw_2 import exceptions
class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 2500

# Добавление атрибутов max_cargo и cargo классу Plane (переопределение родительского)
    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

# Объявление метода load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
# и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
    def load_cargo(self, new_cargo: int):
        current_cargo = self.cargo + new_cargo
        if self.max_cargo < current_cargo:
            raise exceptions.CargoOverload(f"Cargo Overload {current_cargo}, weight limit {self.max_cargo}")
        else:
            self.cargo += new_cargo
            print(f"current weight {current_cargo} tons" )
            return self.cargo

# Объявление метода remove_all_cargo, который принимает число, обнуляет значение cargo и возвращает значение cargo,
# которое было до обнуления
    def remove_all_cargo(self) -> int:
        cargo = self.cargo
        self.cargo = 0
        return cargo

#Отладка сценария через __name__ с помощью интерактивного сеанса Python
if __name__ == '__main__':
    plane = Plane(weight=1000, fuel=100, fuel_consumption=5, max_cargo=2500, cargo=0) # Создание объекта класса Plane
    plane.load_cargo(5)
    print(f"current cargo {plane.load_cargo(5)} tons" )
    print("Plane mro", Plane.__mro__)
