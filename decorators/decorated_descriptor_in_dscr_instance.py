from dataclasses import dataclass

class DecriptoredName:
    def __init__(self, default_value: str):
        self._instances={}
        self.default_value = default_value

    def __get__(self, obj, objtype):
        if obj in self._instances:
          return self._instances[obj]
        else:
          return self.default_value

    def __set__(self, obj, value: str):
        self._instances[obj] = value.lower()

class DecriptorDecorator:
    def __init__(self, descriptor):
        print(f"decorator {descriptor=} is initialized")
        self.descriptor = descriptor

    def __get__(self, obj, objtype):
        returned = self.descriptor.__get__(obj, objtype)
        print(f"get logic, {obj=}, {objtype=}, {returned=}")
        return returned

    def __set__(self, obj, value: str):
        returned = self.descriptor.__set__(obj, value)
        print(f"set logic, {obj=}, {value=}, {returned=}")
        return returned

class PersonWithClassAttr:
    name = DecriptorDecorator(DecriptoredName("ABC"))


if __name__=="__main__":
    Bob = PersonWithClassAttr()
    Martin = PersonWithClassAttr()

    print(f"{Bob.name=}")
    print(f"{Martin.name=}")

    Bob.name = "123"
    Martin.name = "1234"

    print(f"{Bob.name=}")
    print(f"{Martin.name=}")
