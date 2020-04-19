"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from abc import ABC, abstractmethod


class Subscriber(ABC):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got message "{message}"')

    @abstractmethod
    def get_events(self):
        pass


class FullSzamaSubscriber(Subscriber):
    def get_events(self):
        return ['obiad', 'kolacja']


class DietaSubscriber(Subscriber):
    def get_events(self):
        return ['obiad']


class Publisher:
    def __init__(self, events: list):
        self.subscribers = {event: set() for event in events}

    def register(self, subscriber):
        for event in subscriber.get_events():
            self.subscribers[event].add(subscriber)

    def unregister(self, subscriber):
        for event in subscriber.get_events():
            self.subscribers[event].remove(subscriber)

    def dispatch(self, event, message):
        for subscriber in self.subscribers[event]:
            subscriber.update(message)


if __name__ == '__main__':
    publisher = Publisher(['obiad', 'kolacja'])

    tom = FullSzamaSubscriber('Tomek')
    bob = FullSzamaSubscriber('Bobek')
    ola = DietaSubscriber('Ola')
    marta = DietaSubscriber('Marta')

    publisher.register(tom)
    publisher.register(bob)
    publisher.register(ola)
    publisher.register(marta)

    publisher.dispatch('obiad', 'Obiad gotowy')
    publisher.dispatch('kolacja', 'Kolacja gotowa')
