"""
Создать класс Car в модуле car: Класс Car должен быть наследником Vehicle
"""

from Home_W.hw_2.base import Vehicle
from Home_W.hw_2.engine import Engine

# Добавление атрибута engine классу Car
class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, engine: int = 2000):
        super().__init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.engine = engine
        print(self.engine) # Почему не выводит print?

# Объявление метода set_engine, который принимает в себя экземпляр объекта Engine и устанавливает
# на текущий экземпляр Car
    def set_engine(self, engine: Engine):
        self.engine = engine

if __name__ == '__main__':
    print("Car mro", Car.__mro__)
    print("Engine mro", Engine.__mro__)
