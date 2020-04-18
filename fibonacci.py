"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


def fibonacci_cache(fibonacci_function):
    memo_dictionary = {}

    def wrapper(n):
        try:
            return memo_dictionary[n]
        except KeyError:
            memo_dictionary[n] = fibonacci_function(n)
            return memo_dictionary[n]

    return wrapper


@fibonacci_cache
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = fibonacci(5)
    print(fibonacci.__name__)

