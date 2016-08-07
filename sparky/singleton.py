class Singleton(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Create singleton')



def singleton(myClass):
    instances = {}

    def getInstance(*args, **wkargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **wkargs)

        return instances[myClass]

    return getInstance()

@singleton
class TestClass:
    def __init__(self):
        self.x = 10



s = Spam()
c = Spam()

a = TestClass
a.x = 70

b = TestClass
print(b.x)