from itertools import cycle
from sys import maxsize

name_generator = cycle(range(0,maxsize))

def PropertyName(name=None,default=None):
    if name is None:
        name = str(next(name_generator))

    def _get(self):
        try:
            return getattr(self,name)
        except AttributeError:
            return default

    def _set(self, value):
        setattr(self,name,value)

    def _del(self):
        delattr(self,name)
    prop = property(fget=_get,fset=_set,fdel=_del)
    return prop

def DecoratedProperty(descriptor):
    def setter(self, value: str):
        return descriptor.__set__(self, value)

    def getter(self):
        return descriptor.__get__(self).upper()

    def deleter(self):
        return descriptor.__del__(self)
    return property(fget=getter,fset=setter,fdel=deleter)

class Person:
    name = DecoratedProperty(PropertyName(default="abc"))

    def __init__(self, _attr = "dev"):
        self.attr = _attr

if __name__=="__main__":
    Bob = Person()
    Martin = Person()

    print(f"{Bob.name=}")
    print(f"{Martin.name=}")

    Bob.name = "123"
    Martin.name = "1234"

    print(f"{Bob.name=}")
    print(f"{Martin.name=}")
