"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


class Motocycle:
    pass


class Car:
    pass


class Bus:
    pass


class VehicleFactory:
    def __init__(self):
        self.__vehicles = {
            'moto': Motocycle,
            'car': Car,
            'bus': Bus
        }

    def create(self, vehicle_type):
        return self.__vehicles[vehicle_type]()


class VehicleProvider:
    def __init__(self):
        self.__vehicles = {
            'moto': Motocycle(),
            'car': Car(),
            'bus': Bus()
        }

    def get(self, vehicle_type):
        return self.__vehicles[vehicle_type]


if __name__ == '__main__':
    p = VehicleFactory()
    print(id(p.create('bus')))
    print(id(p.create('bus')))
