"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>

Zmień klasę z zadania 3 tak, aby obiekt pojazdu wymagał obiektu drzwi, na podstawie którego utworzysz w pojeździe
tyle drzwi, ile zostało podane w konstruktorze (jak w zadaniu 3)
"""
import copy
from abc import ABC


class Door:
    pass


class Car(ABC):
    def __init__(self, brand, model, number_of_doors, color, door: Door):
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color

        self.__doors = [copy.copy(door) for _ in range(number_of_doors - 1)]
        self.__doors.append(door)

    def doors(self):
        for door in self.__doors:
            print(id(door))

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Fiat(Car):
    def __init__(self, *args, **kwargs):
        super(Fiat, self).__init__('Fiat', *args, **kwargs)


class Audi(Car):
    def __init__(self, *args, **kwargs):
        super(Audi, self).__init__('Audi', *args, **kwargs)


class Rover(Car):
    def __init__(self, *args, **kwargs):
        super(Rover, self).__init__('Rover', *args, **kwargs)


if __name__ == '__main__':
    door = Door()
    fiat = Fiat('panda', 5, 'niebieski', door)
    print(vars(fiat))
    fiat.doors()
