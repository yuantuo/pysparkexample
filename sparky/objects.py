from pprint import pprint
import time
from functools import wraps


class Pairs:

    def __init__(self,*args, **kwargs):
        self.x, self.y = args
        print(kwargs)
        self.day = kwargs['day']
        self.month = kwargs['month']
        self.year = kwargs['year']

    def __repr__(self):
        return( 'Pair({0.x!r},{0.y!r})'.format(self))


    def __str__(self):
        return('String({0.x!r}, {0.y!r})').format(self)


    def __format__(self,code):

        _formats = '{d.day}/{d.month}/{d.year}'
        fmt = _formats
        return fmt.format(d=self)

    """
        use with statments - enter and exit is trigger
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    """
        __slots__ to optimse memeory usage, 428bit to 156
         if your program created millions of instances of a particular class
         unable to add new attr to instance?
         and mulit inhertiance
    """

class A:

    def __init__(self):
        self.x = 2

    def __method(self):
        print('im a method in a')

    def method(self):
        self.__method()

    def spam(self):
        print('A.spam')

    @classmethod
    def timethis(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args)
            #(<__main__.B object at 0x101a04390>, 100000)
            print(kwargs)
            #{}
            start = time.time()
            result = func(*args, **kwargs)
            print(result)
            #1
            end = time.time()
            print(func.__name__, end-start)
            return result
        return wrapper

class B(A):

    def __init__(self):
        super().__init__()
        self.y = 4

    def spam(self):
        print('B.spam')
        super().spam()

    def __method(self):
        print('im a method in b')

    @A.timethis
    def countdown(self, n):
        while n>0:
            n -= 1

        return ('foo', 'bar')


if __name__ == '__main__':

    p = Pairs(2,3, day=23, month=3, year=1983)
    print(p)
    pprint(p)
    print(format(p))

    a = A()
    a.method()
    a.spam()

    b = B()
    b.method()
    b.spam()
    print(b.x)
    print(b.y)

    print(B.__mro__)








    b.countdown(100000)