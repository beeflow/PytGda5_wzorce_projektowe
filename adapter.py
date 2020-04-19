"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from abc import ABC, abstractmethod


class AbstractSubscriber(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subscriber(AbstractSubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got message "{message}"')


class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f'{self.name} dostał(a) wiadomość: "{message}"')


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber: AbstractSubscriber):
        if not isinstance(subscriber, AbstractSubscriber):
            raise RuntimeError('Pfffff')

        self.subscribers.add(subscriber)

    def unregister(self, subscriber: AbstractSubscriber):
        self.subscribers.remove(subscriber)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


class SubscriberTwoAdapter(AbstractSubscriber):
    def __init__(self, name):
        self.subscriber = SubscriberTwo(name)

    def update(self, message):
        self.subscriber.receive(message)


if __name__ == '__main__':
    publisher = Publisher()

    tom = Subscriber('Tomek')
    ola = SubscriberTwoAdapter('Ola')

    publisher.register(tom)
    publisher.register(ola)

    publisher.dispatch('Obiad gotowy')
