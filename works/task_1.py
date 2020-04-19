"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>

Do funkcji „main()” przygotuj dekorator, który każe użytkownikowi podać imię i przekaże to imię do funkcji,
która użyje go zamiast podanego wcześniej imienia:
"""


def get_name(decorated):
    def wrapper(*args, **kwargs):
        return decorated(input('Podaj swoje imię: '))

    return wrapper


@get_name
def main(name: str) -> str:
    return f'Hello, {name}'


if __name__ == '__main__':
    print(main("Rafal"))
