"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


def add_additional_item(equipment_name, equipment_price):
    def car_class_wrapper(car_class):
        class CarWrapper:
            def __init__(self, *args, **kwargs):
                try:
                    kwargs['additional_items'].update({equipment_name: equipment_price})
                except KeyError:
                    kwargs['additional_items'] = {equipment_name: equipment_price}
                self.oInstance = car_class(*args, **kwargs)
                self.__get_result = {}

            def __getattribute__(self, item):
                try:
                    x = super(CarWrapper, self).__getattribute__(item)
                except AttributeError:
                    pass
                else:
                    return self.__calculate_price(x) if item == 'price' else x

                return self.oInstance.__getattribute__(item)

            def __calculate_price(self, price):
                for item_value in self.oInstance.additional_items.values():
                    price += item_value

                return price

            def get(self):
                result = self.oInstance.get()
                if not result:
                    return self.__get_result

                self.__get_result.update(result)
                self.__get_result.update(
                    {item: value for item, value in self.oInstance.additional_items.items()}
                )

                try:
                    del (self.__get_result['additional_items'])
                except KeyError:
                    pass

                return self.__get_result

        return CarWrapper

    return car_class_wrapper


class Car:
    def __init__(self, brand, model, *args, **kwargs):
        self._price = kwargs.pop('price', None)
        self.__brand = brand
        self.__model = model

        for item, value in kwargs.items():
            self.__setattr__(item, value)

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def get(self):
        return {item: value for item, value in self.__dict__.items()}


@add_additional_item('air_conditioner', 1000)
@add_additional_item('seven_seats', 2000)
class BetterCar(Car):
    pass


if __name__ == '__main__':
    fiat = BetterCar('fiat', 'panda', color='niebieski')
    fiat.price = 2000

    print('fiat - additional items:', fiat.additional_items)
    print(f'price of fiat: {fiat.price}')
