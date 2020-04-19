"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>

Przygotuj fabrykę abstrakcyjną dla pojazdów oraz klasę, na podstawie której będzie budowany pojazd.
Zakładamy, że każdy z pojazdów ma informację o marce, modelu, kolorze i ilości drzwi. Do tego przygotuj 3
obiekty samochodów o różnych własnościach.
"""
from abc import ABC


class Car(ABC):
    def __init__(self, brand, model, number_of_doors, color):
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color

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
    def __init__(self, model, number_of_doors, color):
        super(Fiat, self).__init__('Fiat', model, number_of_doors, color)


if __name__ == '__main__':
    fiat = Fiat('panda', 5, 'niebieski')

    print(vars(fiat))
