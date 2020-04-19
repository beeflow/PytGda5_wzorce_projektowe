"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from typing import List


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


class Team:
    def __init__(self, publisher: Publisher, team_members: List[Subscriber]):
        self.publisher = publisher

        for subscriber in team_members:
            self.publisher.register(subscriber)

    def add_member(self, subscriber: Subscriber):
        self.publisher.register(subscriber)

    def dispatch(self, message):
        self.publisher.dispatch(message)


if __name__ == '__main__':
    names = ('Tomek', 'Bobek', 'Ola', 'Marta')
    team_members = [Subscriber(name) for name in names]
    team = Team(Publisher(), team_members)
    team.dispatch('Obiad gotowy')

    team.add_member(Subscriber('Arek'))
    team.dispatch('Kolacja gotowa')
