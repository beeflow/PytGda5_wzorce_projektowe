"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>

Do funkcji „main()” napisz prosty dekorator, który poprosi użytkownika o podanie hasła. Jeżeli hasło nie będzie
zgadzało się z zakładanym (np. 1234), dekorator wyświetli informację o błędnym haśle i nie pozwoli wykonać się 
funkcji „main()”
"""


class AccessDeniedError(RuntimeError):
    pass


def password_required(decorated):
    def wrapper(*args, **kwargs):
        try:
            assert input('Podaj hasło: ') == '1234'
            return decorated(*args, **kwargs)
        except AssertionError:
            raise AccessDeniedError('Incorrect password!')

    return wrapper


@password_required
def main(name: str) -> str:
    return f'Hello, {name}'


if __name__ == '__main__':
    print(main("Rafal"))
