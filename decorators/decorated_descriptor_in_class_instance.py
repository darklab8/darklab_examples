class Undefined:
    pass
undefined = Undefined()

class PropertyName:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __init__(self, default=undefined):
        self._default = default

    @property
    def default(self):
        if self._default is undefined:
            raise AttributeError(f"default value is not defined for {self.public_name=}")
        return self._default

    def __get__(self, obj, objtype=None):
        try:
            value = getattr(obj, self.private_name)
        except AttributeError:
            value = self.default
        return value

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class DecriptorDecorator:
    def __set_name__(self, owner, name):
        setattr(self.descriptor,"public_name", name)
        setattr(self.descriptor,"private_name", f"_{name}")

    def __init__(self, descriptor):
        self.descriptor = descriptor

    def __get__(self, obj, objtype):
        returned = self.descriptor.__get__(obj, objtype)
        print(f"get logic, {obj=}, {objtype=}, {returned=}")
        return returned

    def __set__(self, obj, value: str):
        returned = self.descriptor.__set__(obj, value)
        print(f"set logic, {obj=}, {value=}, {returned=}")
        return returned


class Person:
    name = DecriptorDecorator(PropertyName(default="abc"))
    family = PropertyName(default="yay")
    color = DecriptorDecorator(PropertyName("blue"))

    def __init__(self, _attr = "dev"):
        self.attr = _attr

if __name__=="__main__":
    Bob = Person()
    Martin = Person()

    print(f"{Bob.name=},{Bob.family=}")
    print(f"{Martin.name=},{Martin.family=}")

    Bob.name = "123"
    Bob.family = "asd"
    Martin.name = "1234"
    

    print(f"{Bob.name=},{Bob.family=},{Bob.color=}")
    print(f"{Martin.name=},{Martin.family=},{Martin.color=}")
