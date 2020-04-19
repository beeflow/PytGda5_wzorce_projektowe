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


class Team:
    def __init__(self, publisher, sub_factory, team_members):
        self.publisher = publisher

        for member in team_members:
            self.publisher.register(
                sub_factory.create(member)
            )

    def add_member(self, subscriber: Subscriber):
        self.publisher.register(subscriber)

    def dispatch(self, message):
        self.publisher.dispatch(message)


class SubscriberFactory:
    def create(self, name):
        return Subscriber(name)


if __name__ == '__main__':
    team_members = ('Ania', 'Tomek', 'Paweł', 'Roman')
    team = Team(Publisher(), SubscriberFactory(), team_members)

    team.dispatch('Obiad gotowy')
    print()
    team_members = ('Ania', 'Tomek', 'Paweł', 'Roman', 'Arek')
    kolacja_team = Team(Publisher(), SubscriberFactory(), team_members)

    kolacja_team.dispatch('Kolacja gotowa')
