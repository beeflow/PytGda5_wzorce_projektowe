"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import csv


class Client:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_name(self):
        return f'{self.__first_name} {self.__last_name}'

    def __str__(self):
        return self.get_name()


class ClientFactory:
    def create(self, *args, **kwargs):
        return Client(*args, **kwargs)


class ClientRepository:
    def __init__(self, client_factory: ClientFactory):
        self.__client_factory = client_factory
        self.__clients = set()


    def prepare_clients(self):
        with open('client.csv') as f:
            reader = csv.reader(f)
            for first_name, last_name in reader:
                self.__clients.add(
                    self.__client_factory.create(first_name, last_name)
                )

    def get_clients(self):
        return self.__clients

if __name__ == '__main__':
    repository = ClientRepository(ClientFactory())
    repository.prepare_clients()
    print([client.get_name() for client in repository.get_clients()])