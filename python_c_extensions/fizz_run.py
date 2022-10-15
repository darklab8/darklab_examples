from _fizz.lib import fizz
from _fizz import ffi
import functools
from time import time

def time_measure(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished at {time()-start}")
        return result

    return wrapper

@time_measure
def main():
    result = fizz(1000000)

    # print(f"{result=}")
    print("success")
    print(f"{len(ffi.string(result))=}")

    del result

if __name__=="__main__":
    main()