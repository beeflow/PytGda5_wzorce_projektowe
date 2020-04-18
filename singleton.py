"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


class Singleton:
    def __init__(self, decorated_class):
        self._decorated = decorated_class

    def __call__(self, *args, **kwargs):
        raise TypeError('Singleton must be accessed through `instance()`')

    def __instancecheck__(self, instance):
        return isinstance(instance, self._decorated)

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated
            return self._instance


@Singleton
class Foo:
    def __init__(self):
        print('Created')

    @staticmethod
    def say_hello():
        print('Hello')


if __name__ == '__main__':
    f = Foo.instance()
    g = Foo.instance()

    print(id(f))
    print(id(g))

    print(f'The same? {f is g}')
