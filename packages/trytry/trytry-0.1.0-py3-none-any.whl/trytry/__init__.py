from functools import wraps
from typing import Callable, Dict, Any


class TryTry:

    def __init__(self):
        self.exception_: Dict[Any, Callable] = {}

    def try_(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                handler = None
                for c in self.exception_.keys():
                    if isinstance(e, c):
                        handler = c

                if handler is None:
                    raise e

                return self.exception_[handler](func, e)

        return wrapper

    def except_(self, *exceptions):
        def decorator(f):
            for e in exceptions:
                self.exception_[e] = f
            return f

        return decorator


tryme = TryMe()


@tryme.try_
def my_function():
    print(1 / 0)
    print('hello world')


@tryme.try_
def my_function2():
    print(1 / 0)
    print('hello world')


@tryme.except_(ZeroDivisionError)
def handle_zero_division_error(func, e):
    print(func.__name__, str(e))


if __name__ == '__main__':
    my_function()
    my_function2()
