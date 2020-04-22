"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>

Kod z zadania nr 4 zmodyfikuj w taki sposób, żeby drzwi posiadały informację o tym, czy są zablokowane,
czy nie. Dopisz klasę centralnego zamka, który będzie umiał przesłać sygnał blokowania i odblokowania
do wszystkich drzwi jednocześnie. Pamiętaj, że wszystkie klasy, tj. drzwi, samochód, centralny zamek,
są od siebie niezależne i powinny używać wzorca dependency injection.

Nieznana do tej pory metoda dekorowania za pomocą klasy CarWithCentralLock ;)

Dla ułatwienia, w późniejszych przykładach używam tej wersji.
"""

import copy


class Door:
    def __init__(self):
        self._locked = False

    @property
    def is_locked(self):
        return self._locked

    @property
    def locked_status(self):
        return 'locked' if self._locked else 'unlocked'

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False


class CentralLock:
    def __init__(self):
        self.subscribers = {event: {} for event in ('lock', 'unlock')}

    def register(self, event: str, door_name: str, door: Door):
        self.subscribers[event].update({door_name: door})

    def unregister(self, event: str, door_name: str):
        del self.subscribers[event][door_name]

    def lock(self):
        for door_name, door in self.subscribers['lock'].items():
            door.lock()
            print(f'Door: {door_name} {door.locked_status}')

    def unlock(self):
        for door_name, door in self.subscribers['unlock'].items():
            door.unlock()
            print(f'Door: {door_name} {door.locked_status}')


class Car:
    _possible_doors = ('front left', 'front right', 'rear left', 'rear right', 'trunk')

    def __init__(self, brand, model, number_of_doors, door: Door, color):
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color

        self.__doors = {self._possible_doors[i]: copy.copy(door) for i in range(number_of_doors - 1)}
        self.__doors.update({self._possible_doors[-1]: door})

    def lock(self, door_name):
        """Klasa zyskała metodę do zamykania drzwi."""
        self.__doors[door_name].lock()
        print(f'Door: {door_name} {self.__doors[door_name].locked_status}')

    def unlock(self, door_name):
        """Klasa zyskała metodę do otwierania drzwi."""
        self.__doors[door_name].unlock()
        print(f'Door: {door_name} {self.__doors[door_name].locked_status}')

    def doors(self):
        for door_name, door in self.__doors.items():
            print(f'{door_name}: {id(door)}')

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


class CarWithCentralLock(Car):
    """Wzorzec dekorator poprzez udekorowanie klasy inną klasą."""

    def __init__(self, car: Car, central_lock: CentralLock):
        self.car = car
        self.central_lock = central_lock

        for door_name, door in self.car._Car__doors.items():
            self.central_lock.register('lock', door_name, door)
            self.central_lock.register('unlock', door_name, door)

    def doors(self):
        self.car.doors()

    def lock(self, *args, **kwargs):
        self.central_lock.lock()

    def unlock(self, *args, **kwargs):
        self.central_lock.unlock()


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
    central_lock = CentralLock()
    fiat = CarWithCentralLock(Fiat('panda', 3, door, 'niebieski'), central_lock)

    fiat.doors()

    fiat.lock('front left')
    print('-----------')
    fiat.unlock('front left')
