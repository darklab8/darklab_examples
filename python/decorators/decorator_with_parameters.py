from enum import Enum, auto
from typing import Protocol
import abc


class RuntimeState(Enum):
    STARTING = auto()
    STARTED = auto()
    STOPPING = auto()
    STOPPED = auto()
    UNDEFINED = auto()

def stateful(intial_state, finished_state):
    def decorator(function):
        def wrapper(self, *args, **kwargs):
            self.state = intial_state
            result = function(self, *args, **kwargs)
            self.state = finished_state
            return result
        return wrapper
    return decorator


class StateDescriptor:

    def __set_name__(self, owner, name):
        self.set_name(name)

    def set_name(self, name):
        self.public_name = name
        self.private_name = '_' + name

    def __init__(self, default):
        self.default = default

    def __get__(self, obj, objtype=None):
        try:
            value = getattr(obj, self.private_name)
        except AttributeError:
            value = self.default
        return value

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)
        print(f"{getattr(obj, self.private_name)}")

class Component(abc.ABC):
    state = StateDescriptor(RuntimeState.UNDEFINED)

    @abc.abstractmethod
    def _start(self):
        pass

    @abc.abstractmethod
    def _stop(self):
        pass

    @stateful(RuntimeState.STARTING, RuntimeState.STARTED)
    def start(self):
        self._start()
    
    @stateful(RuntimeState.STOPPING, RuntimeState.STOPPED)
    def stop(self):
        self._stop()


class ConcreteComponent(Component):
    
      
    def _start(self):
        pass
        # Some code that starts the component goes here.

    def _stop(self):
        pass
        # Some code that shutsdown the component here.

if __name__=="__main__":

    a = ConcreteComponent()
    a.start()
    a.stop()