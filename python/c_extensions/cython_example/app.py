from hello import say_hello_to
from hello import fib

say_hello_to("abc")
fib(4)

import pyximport; pyximport.install()
from imported_world import hello_world

hello_world("qwe")