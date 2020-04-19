"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got message "{message}"')


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == '__main__':
    publisher = Publisher()

    tom = Subscriber('Tomek')
    bob = Subscriber('Bobek')
    ola = Subscriber('Ola')
    marta = Subscriber('Marta')

    publisher.register(tom)
    publisher.register(bob)
    publisher.register(ola)
    publisher.register(marta)

    publisher.dispatch('Obiad gotowy')

    publisher.unregister(ola)
    publisher.unregister(marta)

    publisher.dispatch('Kolacja gotowa')