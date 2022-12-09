from hello_lib import fib
from pydantic import BaseModel

class Hello(BaseModel):
    abc: int = 123

def say_hello_to(name):
    print(f"Hello %s!, {Hello}" % name)
